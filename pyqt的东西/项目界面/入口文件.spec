# -*- mode: python -*-

block_cipher = None


a = Analysis(['����ļ�.py'],
             pathex=['C:\\Users\\36554\\Desktop\\python�ܽ�\\pyqt�Ķ���\\��Ŀ����'],
             binaries=[],
             datas=[],
             hiddenimports=['pyqt�Ķ���'],
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
          name='����ļ�',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
