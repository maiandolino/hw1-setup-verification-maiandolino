#!/usr/bin/env python3
"""
RosettaML Bootcamp 2025 - HW2: PyMOL and VS Code Setup Verification
This script verifies that PyMOL and VS Code are installed and working correctly.
"""

import sys
import os
import platform
import subprocess
from datetime import datetime

def check_command(command, name):
    """
    Check if a command is available in the system PATH.

    Args:
        command: The command to check (e.g., 'pymol', 'code')
        name: Display name for the command

    Returns:
        tuple: (success: bool, version: str, error_msg: str)
    """
    try:
        # Try to run the command with --version
        result = subprocess.run(
            [command, '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            version = result.stdout.strip() or result.stderr.strip()
            return True, version, None
        else:
            return False, None, f"Command '{command}' not found or not working"

    except FileNotFoundError:
        return False, None, f"Command '{command}' not found in PATH"
    except subprocess.TimeoutExpired:
        return False, None, f"Command '{command}' timed out"
    except Exception as e:
        return False, None, str(e)

def check_file_exists(filename):
    """Check if a required file exists in the current directory."""
    return os.path.isfile(filename)

def main():
    print("=" * 70)
    print("RosettaML Bootcamp 2025 - PyMOL and VS Code Setup Verification")
    print("=" * 70)
    print()
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Current Directory: {os.getcwd()}")
    print()

    results = {
        'timestamp': datetime.now().isoformat(),
        'student_name': 'REPLACE_WITH_YOUR_NAME',
        'python_version': sys.version,
        'platform': platform.platform(),
        'checks': {}
    }

    all_passed = True

    # Check PyMOL
    print("Checking PyMOL installation...")
    print("-" * 70)

    pymol_success, pymol_version, pymol_error = check_command('pymol', 'PyMOL')
    results['checks']['pymol'] = {
        'installed': pymol_success,
        'version': pymol_version,
        'error': pymol_error
    }

    if pymol_success:
        print("✓ PASS PyMOL is installed")
        if pymol_version:
            print(f"         Version info: {pymol_version[:100]}")
    else:
        print("✗ FAIL PyMOL command not found")
        print(f"         Error: {pymol_error}")
        print("         Note: PyMOL might be installed but not in your PATH")
        all_passed = False

    print()

    # Check VS Code
    print("Checking VS Code installation...")
    print("-" * 70)

    vscode_success, vscode_version, vscode_error = check_command('code', 'VS Code')
    results['checks']['vscode'] = {
        'installed': vscode_success,
        'version': vscode_version,
        'error': vscode_error
    }

    if vscode_success:
        print("✓ PASS VS Code is installed")
        if vscode_version:
            print(f"         Version: {vscode_version[:100]}")
    else:
        print("✗ FAIL VS Code 'code' command not found")
        print(f"         Error: {vscode_error}")
        print("         Note: VS Code might be installed but 'code' command not in PATH")
        print("         See troubleshooting in README.md")
        all_passed = False

    print()

    # Check for required submission files
    print("Checking for required submission files...")
    print("-" * 70)

    required_files = {
        '1ubq_session.pse': 'PyMOL session file',
        '1ubq_visualization.png': 'PyMOL visualization image'
    }

    files_present = {}
    for filename, description in required_files.items():
        exists = check_file_exists(filename)
        files_present[filename] = exists

        if exists:
            size = os.path.getsize(filename)
            print(f"✓ PASS {filename} found ({size} bytes)")
        else:
            print(f"✗ FAIL {filename} not found")
            print(f"         Create this file as described in README.md")
            all_passed = False

    results['checks']['files'] = files_present

    print("-" * 70)
    print()

    # Generate verification output file
    output_file = 'verification_result.txt'

    try:
        with open(output_file, 'w') as f:
            f.write("=" * 70 + "\n")
            f.write("RosettaML Bootcamp 2025 - HW2 Verification Results\n")
            f.write("=" * 70 + "\n\n")

            f.write(f"Student Name: {results['student_name']}\n")
            f.write(f"Timestamp: {results['timestamp']}\n")
            f.write(f"Python Version: {results['python_version']}\n")
            f.write(f"Platform: {results['platform']}\n\n")

            f.write("Installation Checks:\n")
            f.write("-" * 70 + "\n")

            for tool, check in results['checks'].items():
                if tool == 'files':
                    continue
                f.write(f"\n{tool.upper()}:\n")
                f.write(f"  Installed: {check['installed']}\n")
                if check['version']:
                    f.write(f"  Version: {check['version'][:200]}\n")
                if check['error']:
                    f.write(f"  Error: {check['error']}\n")

            f.write("\nFile Checks:\n")
            f.write("-" * 70 + "\n")
            for filename, exists in files_present.items():
                status = "Present" if exists else "Missing"
                f.write(f"  {filename}: {status}\n")

            f.write("\n" + "=" * 70 + "\n")
            if all_passed:
                f.write("STATUS: ALL CHECKS PASSED ✓\n")
            else:
                f.write("STATUS: SOME CHECKS FAILED ✗\n")
            f.write("=" * 70 + "\n")

        print(f"✓ Verification file created: {output_file}")
        print()

        if all_passed:
            print("🎉 SUCCESS! All checks passed!")
            print()
            print("Next steps:")
            print("1. Open 'verification_result.txt' and replace 'REPLACE_WITH_YOUR_NAME' with your actual name")
            print("2. Make sure you have all required files:")
            print("   - 1ubq_session.pse")
            print("   - 1ubq_visualization.png")
            print("   - verification_result.txt")
            print("3. Commit and push your files:")
            print("   git add 1ubq_session.pse 1ubq_visualization.png verification_result.txt")
            print("   git commit -m 'Complete PyMOL and VS Code setup verification'")
            print("   git push")
            print()
            return 0
        else:
            print("⚠️  Some checks failed - see details above.")
            print()
            print("Please complete all tasks described in README.md and run this script again.")
            print()
            return 1

    except Exception as e:
        print(f"❌ Error creating verification file: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())