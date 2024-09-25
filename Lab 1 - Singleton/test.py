from generate import generate
import subprocess

for i in range(100):
    fileName = generate()
    command = ["python", "slangel_lab1.py", fileName]

    # Execute the command
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        expecting = fileName.split('e')

        expected_value = expecting[1].strip()  # Strip whitespace
        result_output = result.stdout.strip()  # Strip whitespace
        if expected_value == result_output:
            print("Passed")
        else:
            print("FAILED")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command for file: {fileName}\n{e.stderr}")
