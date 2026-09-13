import os, sys
base = r"C:/Users/Alexa/AppData/Local/hermes/profiles"
profiles = sorted([d for d in os.listdir(base) if os.path.isdir(os.path.join(base,d))])
print("PROFILES:", profiles)
for p in profiles:
    d = os.path.join(base,p)
    files = sorted(os.listdir(d))
    has_soul = "SOUL.md" in files
    has_user = "USER.md" in files
    has_memory = "MEMORY.md" in files
    has_profile_yaml = "profile.yaml" in files
    has_config_yaml = "config.yaml" in files
    print(f"\n===== PROFILE: {p} =====")
    print(f"  files: {files}")
    if has_soul:
        with open(os.path.join(d,"SOUL.md"), "r") as f:
            s = f.read()
        print(f"  SOUL.md lines={len(s.splitlines())} chars={len(s)}")
        for l in s.splitlines()[:12]:
            print(f"      {l}")
    else:
        print(f"  SOUL.md: MISSING")
    if has_profile_yaml:
        with open(os.path.join(d,"profile.yaml"), "r") as f:
            py = f.read()
        print(f"  profile.yaml present: yes")
        for l in py.splitlines():
            print(f"      {l}")
    else:
        print(f"  profile.yaml: MISSING")
    if has_config_yaml:
        with open(os.path.join(d,"config.yaml"), "r") as f:
            lines = f.read().splitlines()
        for l in lines:
            if any(k in l for k in ["default_model","provider:","model:","base_url"]):
                print(f"  config.yaml: {l}")
