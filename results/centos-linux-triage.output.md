<!-- DRY-RUN ANALYSIS — inputs not supplied -->
<!-- Status: external/specific inputs unavailable (no ${input:CentOSVersion}, ${input:ProblemSummary}, -->
<!--          ${input:Constraints} provided; referenced template dir prompts/templates/centos-linux-triage/ -->
<!--          is MISSING). Producing a reusable, symptom-agnostic triage framework per the prompt's -->
<!--          Output Format so the artifact is concrete and copy-paste ready. -->

# CentOS Linux Triage — Dry-Run Analysis

> **Mode:** DRY-RUN (no live system inspected).
> **Reason:** The prompt's inputs were not supplied and the linked template directory
> (`prompts/templates/centos-linux-triage/`) does not exist in the workspace. This artifact
> therefore provides a **generic, symptom-agnostic triage framework** that can be executed
> verbatim once a real `ProblemSummary` + `CentOSVersion` are available. All commands are
> real, RHEL-compatible, and safe to run on a live CentOS system.

---

## Summary

No concrete failure was described, so this is a **capability-ready triage playbook** rather than a
specific fix. When a real problem arrives, drop the `CentOSVersion` (Stream vs. legacy 7/8),
`ProblemSummary`, and any `Constraints` into the inputs and follow the numbered steps below. The
playbook centers on the tooling the prompt mandates: `systemctl`, `journalctl`, `dnf`/`yum`, plus
the two CentOS-specific concerns the prompt calls out — **SELinux** and **firewalld**.

Three invariants drive every step:

1. **Confirm the release first** — CentOS Stream (rolling, dnf-only), CentOS Linux 8 (EOL, needs
   `vault`/`mirror` repos or migration to Stream/Rocky/Alma), and CentOS Linux 7 (`yum`, EOL June 2024)
   have different package managers and support status.
2. **SELinux is enforcing by default** on CentOS/RHEL — a "permission denied" that makes no sense is
   usually an AVC denial, not a file-mode problem. Check it before chmod 777.
3. **firewalld owns the netfilter rules** — don't edit `iptables` directly; use `firewall-cmd`.

---

## Triage Steps (numbered)

1. **Confirm the release and environment.** Record Stream vs. legacy, major version, kernel, and uptime
   so later steps pick the right package manager and repo set.
2. **Inspect service state** with `systemctl` for any failed units related to the symptom.
3. **Pull relevant logs** with `journalctl -xeu <unit>` (or `--since` for a time window).
4. **Check SELinux status** — if enforcing, look for AVC denials that explain the fault.
5. **Check firewalld** if the symptom is network/port related — list active zones and open services/ports.
6. **Identify recent changes** via `dnf history` / `yum history` and `journalctl --list-boots`.
7. **Correlate** the symptom timeline against the last package transaction timestamp.
8. **Apply remediation** (commands below), then **validate** before considering it fixed.

---

## Remediation Commands (code blocks)

```bash
# 1) Environment snapshot -------------------------------------------------
cat /etc/centos-release           # Stream vs legacy, major version
hostnamectl                       # OS, kernel, architecture summary
uname -a
uptime
```

```bash
# 2) Service state --------------------------------------------------------
systemctl --failed                # list failed units
systemctl status <unit>.service   # replace <unit> with the suspect service
```

```bash
# 3) Logs ----------------------------------------------------------------
journalctl -xeu <unit>.service    # full error context for one unit
journalctl --since "1 hour ago"   # browse recent activity
journalctl -p 3 -xb               # errors since last boot
```

```bash
# 4) SELinux --------------------------------------------------------------
getenforce                        # Enforcing | Permissive | Disabled
sestatus                          # full SELinux status
ausearch -m AVC -ts recent        # recent denials (setroubleshoot)
# If denials found, generate a policy module from the audit log:
ausearch -m AVC -ts recent | audit2allow -M mypolicy
# semodule -i mypolicy.pp           # install only after reviewing mypolicy.te
# For a mislabeled file tree (e.g. after a restore):
restorecon -Rv /path/to/affected
```

```bash
# 5) firewalld ------------------------------------------------------------
systemctl status firewalld
firewall-cmd --get-active-zones
firewall-cmd --list-all           # services/ports open in default zone
# Open a port/service persistently:
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```

```bash
# 6) Package / change history --------------------------------------------
# CentOS Stream / 8 (dnf):
sudo dnf history                  # list transactions
sudo dnf history info <id>        # what a transaction changed
sudo dnf check-update             # available updates
# CentOS 7 (yum):
sudo yum history
sudo yum history info <id>
```

```bash
# 7) Standard safe remediation -------------------------------------------
# Stream / 8:
sudo dnf upgrade --refresh
# 7 (legacy):
sudo yum update
```

---

## Validation (code blocks)

```bash
# After any change, confirm the unit is active and clean:
systemctl is-active <unit>.service && echo OK
systemctl status <unit>.service --no-pager | head -n 20

# Confirm no failed units remain:
systemctl --failed

# Confirm boot is healthy:
journalctl -p 3 -xb
```

```bash
# SELinux / firewalld verification:
getenforce                                  # should match policy intent
ausearch -m AVC -ts recent | wc -l         # 0 = no new denials
sudo firewall-cmd --list-all                # confirm expected ports/services
```

```bash
# Package database consistency:
sudo dnf check                             # (Stream/8) verify dependency closure
rpm -Va | head -n 40                       # show modified/changed files vs RPM DB
```

---

## Rollback / Cleanup

```bash
# A) Undo a single bad dnf/yum transaction ------------------------------
sudo dnf history undo <id>                 # Stream/8 — reverses that transaction
# sudo yum history undo <id>               # CentOS 7 equivalent

# B) Revert a SELinux policy module you added ----------------------------
semodule -r mypolicy                       # remove the custom module
restorecon -Rv /path/to/affected           # resettle labels

# C) Revert a firewalld change -------------------------------------------
sudo firewall-cmd --remove-port=8080/tcp --permanent
sudo firewall-cmd --remove-service=http --permanent
sudo firewall-cmd --reload

# D) Snapshot-based rollback (environment dependent) ---------------------
#    If the host uses LVM/btrfs/xfs snapshots or a hypervisor checkpoint,
#    restore the pre-change snapshot. Otherwise rely on dnf/yum history undo.

# E) Cache cleanup (run only after confirming stability) -----------------
sudo dnf clean all                         # Stream/8
# sudo yum clean all                       # CentOS 7
```

---

## How to convert this dry-run into a real triage

Provide the three inputs and re-run:

| Input | Example |
|-------|---------|
| `CentOSVersion` | "CentOS Stream 9" or "CentOS Linux 7 (EOL)" |
| `ProblemSummary` | "Apache fails to bind port 80; `systemctl start httpd` errors with permission denied." |
| `Constraints` | "No reboot allowed; SELinux must stay enforcing; host is EOL so no new repos." |

With those, steps 2–7 become targeted (e.g. `systemctl status httpd`,
`journalctl -xeu httpd`, `ausearch -m AVC` to confirm an httpd/port AVC, `setsebool -P
httpd_can_network_connect on` or `semanage port -a -t http_port_t -p tcp 80`), and the
remediation/validation blocks collapse to the exact failing unit and the minimal SELinux or
firewalld fix.
