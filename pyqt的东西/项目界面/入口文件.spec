# -*- mode: python -*-

block_cipher = None


a = Analysis(['入口文件.py'],
             pathex=['C:\\Users\\36554\\Desktop\\python总结\\pyqt的东西\\项目界面'],
             binaries=[],
             datas=[],
             hiddenimports=['pyqt的东西'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='入口文件',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
