import subprocess, sys

CMDS = [
    [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
    [sys.executable, 'src/data_download.py'],
    [sys.executable, 'src/run_experiments.py', '--config', 'configs/default.yaml'],
    [sys.executable, 'src/plot_forecasts.py']
]

def main():
    for c in CMDS:
        print('\n>>>', ' '.join(c))
        r = subprocess.run(c)
        if r.returncode != 0:
            print('Command failed:', c)
            sys.exit(r.returncode)
    print('\nDone. See reports/.')

if __name__ == '__main__':
    main()
