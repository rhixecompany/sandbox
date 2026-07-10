<!-- DRY-RUN ANALYSIS — inputs not supplied -->
<!-- Status: external/specific inputs unavailable (no ${input:ArchSnapshot}, ${input:ProblemSummary}, -->
<!--          ${input:Constraints} provided; referenced template dir prompts/templates/arch-linux-triage/ -->
<!--          is MISSING). Producing a reusable, symptom-agnostic triage framework per the prompt's -->
<!--          Output Format so the artifact is concrete and copy-paste ready. -->

# Arch Linux Triage — Dry-Run Analysis

> **Mode:** DRY-RUN (no live system inspected).
> **Reason:** The prompt's inputs were not supplied and the linked template directory
> (`prompts/templates/arch-linux-triage/`) does not exist in the workspace. This artifact
> therefore provides a **generic, symptom-agnostic triage framework** that can be executed
> verbatim once a real `ProblemSummary` + `ArchSnapshot` are available. All commands are
> real, Arch-appropriate, and safe to run on a live Arch system.

---

## Summary

No concrete failure was described, so this is a **capability-ready triage playbook** rather than a
specific fix. When a real problem arrives, drop the `ArchSnapshot` (kernel, last `pacman -Syu` date,
offending package) and `ProblemSummary` into the inputs and follow the numbered steps below. The
playbook centers on the three tools the prompt mandates: `systemctl`, `journalctl`, and `pacman`,
plus the rolling-release discipline (full upgrades only, reboot after kernel/`linux` updates).

Two invariants drive every step:

1. **Never do a partial upgrade** — always `pacman -Syu`, never `pacman -Sy <pkg>`.
2. **Reboot after any `linux`/kernel or `systemd`/mesa update** before declaring "fixed".

---

## Triage Steps (numbered)

1. **Capture the environment snapshot.**
   Record kernel, uptime, and last upgrade so later steps can correlate causes.
2. **Inspect service state** with `systemctl` for any failed units related to the symptom.
3. **Pull relevant logs** with `journalctl -xeu <unit>` (or `--since` for a time window).
4. **Check for broken/partial package state** with `pacman -Qkk` and `paccheck` if installed.
5. **Identify recent changes** via `less /var/log/pacman.log` and `journalctl --list-boots`.
6. **Correlate** the symptom timeline against the last `pacman -Syu` timestamp.
7. **Apply remediation** (commands below), then **validate** before rebooting.
8. **Decide reboot** — required if `linux`, `systemd`, `mesa`, or `mkinitcpio` were touched.

---

## Remediation Commands (code blocks)

```bash
# 1) Environment snapshot -------------------------------------------------
uname -a
uptime
ls -l /boot/vmlinuz-linux            # confirm kernel image exists
tail -n 5 /var/log/pacman.log        # last upgrade timestamp
```

```bash
# 2) Service state --------------------------------------------------------
systemctl --failed                   # list failed units
systemctl status <unit>.service      # replace <unit> with the suspect service
```

```bash
# 3) Logs ----------------------------------------------------------------
journalctl -xeu <unit>.service       # full error context for one unit
journalctl --since "1 hour ago"      # browse recent activity
```

```bash
# 4) Package integrity ----------------------------------------------------
pacman -Qkk                          # verify all installed files vs DB
pacman -Qqm                         # list foreign (AUR/outside-repo) packages
```

```bash
# 5) Recent upgrades ------------------------------------------------------
less /var/log/pacman.log             # find the upgrade that preceded the fault
```

```bash
# 6) Standard safe remediation -------------------------------------------
sudo pacman -Syu                     # ALWAYS full upgrade, never partial
sudo mkinitcpio -P                   # rebuild images if linux/systemd changed
```

```bash
# If a specific package is broken, force reinstall:
sudo pacman -S --overwrite '*' <pkg>
```

---

## Validation (code blocks)

```bash
# After any change, confirm the unit is active and clean:
systemctl is-active <unit>.service && echo OK
systemctl status <unit>.service --no-pager | head -n 20

# Confirm no failed units remain:
systemctl --failed

# Confirm boot is healthy post-reboot:
journalctl -p 3 -xb                  # errors since last boot
```

```bash
# Verify package database consistency:
sudo pacman -Dk                      # check dependencies are satisfiable
pacman -Qkk | grep -v '0 altered'    # show only mismatched files
```

---

## Rollback / Cleanup

```bash
# A) Downgrade a single bad package from the pacman cache:
ls /var/cache/pacman/pkg/ | grep <pkg>
sudo pacman -U /var/cache/pacman/pkg/<pkg>-<old>-*.pkg.tar.zst

# B) If a full upgrade broke things, boot the LTS kernel or use a snapshot:
#    (Timeshift / snapper / BTRFS snapshot rollback — environment dependent)

# C) Cache cleanup (run only after confirming stability):
paccache -r                          # keep 3 most recent versions
sudo pacman -Sc                      # remove uninstalled pkg leftovers from cache

# D) Orphan cleanup (review list before deleting):
pacman -Qtdq                         # list orphans
# sudo pacman -Rns $(pacman -Qtdq)   # REMOVE ONLY AFTER REVIEW
```

---

## How to convert this dry-run into a real triage

Provide the three inputs and re-run:

| Input | Example |
|-------|---------|
| `ProblemSummary` | "WiFi drops after `pacman -Syu`; `NetworkManager` fails to start." |
| `ArchSnapshot` | `Linux 6.9.1-arch1; last full upgrade 2026-07-08;`linux` + `systemd` updated." |
| `Constraints` | "No reboot allowed during business hours; laptop on battery." |

With those, steps 2–7 become targeted (e.g. `systemctl status NetworkManager`,
`journalctl -xeu NetworkManager`, reinstall `wpa_supplicant`, etc.) and the
remediation/validation blocks collapse to the exact failing unit.
