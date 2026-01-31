Folder Structure 
steganography-tool/
│
├── encode.py        # Hide message in image
├── decode.py        # Extract hidden message
├── utils.py         # Helper functions
├── requirements.txt
├── README.md
└── samples/
    ├── input.png
    └── output.png

Execution:
FOR ENCODE:
python encode.py

FOR DECODE:
python decode.py

CREATE VIRTUAL ENVIRONMENT:
python -m venv venv
venv\Scripts\activate   # Windows

INSTALL REQUIRED LIBRARIES:
pip install pillow
