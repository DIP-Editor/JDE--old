# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['JDE.py'],
    pathex=[],
    binaries=[],
    datas=[('settings.txt', '.'), ('keywords.txt', '.'), ('run.png', '.'), ('clear_terminal.png', '.'), ('clear_text.png', '.'), ('color_mode.png', '.'), ('copy.png', '.'), ('create_template.png', '.'), ('delete_template.png', '.'), ('find_and_replace.png', '.'), ('open_template.png', '.'), ('open.png', '.'), ('paste.png', '.'), ('quit.png', '.'), ('report_bug.png', '.'), ('save_as.png', '.'), ('save.png', '.'), ('settings.png', '.'), ('reset.png', '.'), ('export_template.png', '.'), ('extensions.png', '.'), ('color_theme.txt', '.'), ('font.txt', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='JDE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='JDE.icns',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='JDE',
)
app = BUNDLE(
    coll,
    info_plist={
                'CFBundleDocumentTypes': [
            {
                'CFBundleTypeExtensions': ['py', 'txt'],
                'CFBundleTypeName': 'Python Script', 
                'CFBundleTypeRole': 'Editor',
                'CFBundleTypeOSTypes': ['TEXT'],
            },
        ],
    },
    name='JDE.app',
    icon='JDE.icns',
    bundle_identifier=None,
)
