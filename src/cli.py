import os
from pathlib import Path
from src import db

MICROSCOPE_MAP = {
    '1': ('Light Microscope (40x)', 40.0),
    '2': ('Compound Microscope (100x)', 100.0),
    '3': ('Electron Microscope (1000x)', 1000.0),
    '4': ('Scanning EM (20000x)', 20000.0)
}

UNIT_CONVERSIONS = {
    'nm': 1e6,
    'um': 1e3,
    'mm': 1.0,
    'cm': 0.1,
    'm': 0.001
}

def choose_from_map(prompt, options):
    print(prompt)
    for k, (name, *_) in options.items():
        print(f"  {k}. {name}")
    choice = input('Enter choice number: ').strip()
    if choice not in options:
        print('Invalid selection')
        return choose_from_map(prompt, options)
    return choice

def choose_unit():
    keys = list(UNIT_CONVERSIONS.keys())
    for i, k in enumerate(keys, 1):
        print(f"  {i}. {k}")
    idx = input('Choose unit number: ').strip()
    try:
        idx = int(idx)
        if 1 <= idx <= len(keys):
            return keys[idx-1]
    except Exception:
        pass
    print('Invalid selection')
    return choose_unit()

def run_cli():
    db.init_db()
    print('Microscope Specimen Size Calculator (CLI)')
    username = input('Enter your username: ').strip()
    if not username:
        print('Username required')
        return
    image_path = input('Enter specimen image path (or leave empty): ').strip()
    if image_path:
        p = Path(image_path)
        if not p.exists():
            print('Warning: image path does not exist. Continue? (y/n)')
            if input().lower() != 'y':
                return
    measured = input('Enter measured specimen size seen in microscope (in mm): ').strip()
    try:
        measured_mm = float(measured)
    except Exception:
        print('Invalid number')
        return
    choice = choose_from_map('Select microscope type:', MICROSCOPE_MAP)
    name, mag = MICROSCOPE_MAP[choice]
    unit = choose_unit()

    real_mm = measured_mm / mag
    converted = real_mm * UNIT_CONVERSIONS[unit]

    print('\nResult')
    print('------')
    print(f'User: {username}')
    print(f'Microscope: {name} (magnification {mag}x)')
    print(f'Measured (mm): {measured_mm:.6g} mm')
    print(f'Calculation: real = measured_mm / magnification => {measured_mm} / {mag} = {real_mm} mm')
    print(f'Result: {converted:.6g} {unit}')

    db.insert_record(username, image_path or None, measured_mm, real_mm, unit)
    print('Saved to database.')

if __name__ == '__main__':
    run_cli()
