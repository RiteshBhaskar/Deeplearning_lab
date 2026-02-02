print(f"Current Python Path: {sys.executable}")

# This checks if a Conda environment is active in the shell
conda_env = os.environ.get('CONDA_DEFAULT_ENV')

if conda_env:
    print(f"Active Conda Environment: {conda_env}")
else:
    print("No Conda environment detected (using Global/System Python).")
print("my name is mac ,hello world ")
