from distutils.core import setup, Extension


def main():
    setup(name="qmcdump",
          version="0.1",
          description="Convert qmc to mp3",
          author="taodi",
          author_email="mlzgg@sina.com",
          ext_modules=[Extension("qmcdump", ["src/qmcdump.cpp"])])


if __name__ == "__main__":
    main()
