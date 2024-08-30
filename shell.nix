let
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-23.11.tar.gz") {};
in
  pkgs.mkShell {
    buildInputs = with pkgs; [
      # Python with packages
      (python3.withPackages (ps:
        with ps; [
          tkinter
          pillow
          pip
        ]))

      xorg.libX11
      xorg.libXext
      xorg.libXrender
      xorg.libXinerama
      xorg.libXcursor
      xorg.libXi
      xorg.libXrandr
    ];

    shellHook = ''
      export PIP_PREFIX=$(pwd)/_python_env
      export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
      export PATH="$PIP_PREFIX/bin:$PATH"
      unset SOURCE_DATE_EPOCH

      echo "Nix environment for Raspberry Pi Python Tkinter app is ready!"
      echo "Python version: $(python3 --version)"
      echo "To install sv-ttk, run: pip install sv-ttk"
      echo "To run your app, use: python3 your_script_name.py"
    '';
  }
