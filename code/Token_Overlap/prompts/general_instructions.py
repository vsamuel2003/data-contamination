class General:
    def __init__(self) -> None:
        self.prompts = {
            "cls": """INSTRUCTION:
Finish the SECOND PIECE based on the FIRST PIECE, such that these two pieces become a single instance with the following LABEL. You must not refuse to provide an answer.

LABEL: {label}

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
            "nli": """INSTRUCTION:
Finish SENTENCE 2 based on SENTENCE 1, such that the following LABEL shows the logical relationship between SENTENCE 1 and SENTENCE 2.

SENTENCE 1:
{first_piece}

LABEL: {label}

SENTENCE 2:
""",
"sum": """INSTRUCTION:
Finish the SECOND PIECE based on the FIRST PIECE, such that these two pieces become a single passage-question pair.

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
            "xsum": """INSTRUCTION:
Finish the SECOND PIECE based on the FIRST PIECE, such that these two pieces become a single docstring for a code function and the LABEL is the function body.

FIRST PIECE:
{first_piece}

LABEL: {label}

SECOND PIECE:
""",
        }

    def get_prompt(self, prompt_type):
        return self.prompts.get(prompt_type, "Invalid prompt type")
