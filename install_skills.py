"""
Antigravity Skills Installer
Cross-platform helper script to install skills into your local agent environment.
"""

import os
import shutil
import sys
from pathlib import Path

def get_default_skills_dir():
    home = Path.home()
    # Check Antigravity / Gemini paths
    default_path = home / ".gemini" / "skills"
    return default_path

def install_skills(source_domain=None, target_dir=None):
    if target_dir is None:
        target_dir = get_default_skills_dir()

    target_dir.mkdir(parents=True, exist_ok=True)
    repo_root = Path(__file__).parent.resolve()

    # Find directories
    domain_dirs = [d for d in repo_root.iterdir() if d.is_dir() and not d.name.startswith('.')]

    if source_domain:
        matched = [d for d in domain_dirs if source_domain.lower() in d.name.lower()]
        if not matched:
            print(f"No domain matched '{source_domain}'. Available domains:")
            for d in domain_dirs:
                print(f"  - {d.name}")
            return
        domain_dirs = matched

    installed_count = 0
    for domain_dir in domain_dirs:
        print(f"Processing domain: {domain_dir.name}...")
        for skill_dir in domain_dir.iterdir():
            if skill_dir.is_dir():
                dest = target_dir / skill_dir.name
                shutil.copytree(skill_dir, dest, dirs_exist_ok=True)
                installed_count += 1

    print(f"\nSuccessfully installed {installed_count} skills to {target_dir}")

if __name__ == "__main__":
    domain_arg = sys.argv[1] if len(sys.argv) > 1 else None
    install_skills(source_domain=domain_arg)
