pertubation_prompts = {
"MMLU": '''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and overall structure of the four options must exactly match every detail and the structure in the Input Text. You must not include the provided Input Text as an option. Each option in the four-question quiz you generate must include both the underlying text and answer choices in the Input Text but with word-level pertubations.
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations. 
(3) Each Option must still include the main part of the text in the Input Text with word level pertubations
(4) Each option must still include all answer choices present in the Input Text with word level pertubations
(5) No numbers or proper nouns are changed.
(6) Options are ordered;
(7) There is not any extra explanation;
(8) You comply with the following "Format" to generate options
(9) You comply with every specific symbol and letter detail in the given Input Text; and 
(10) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
''',
"HumanEval": '''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and sentence structure of the four options must exactly match every detail in the Input Text. You must not include the provided Input Text as an option. 
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations.
(3) All spacing (such as '\n' and '\t') and formatting for each options must be the exact same as that of the Input Text
(4) Options are ordered;
(5) There is not any extra explanation;
(6) You follow the following ”Format” to generate options;
(7) You comply with every specific symbol and letter detail in the given Input Text; and 
(8) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
''',
"DROP":'''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and sentence structure of the four options must exactly match every detail in the Input Text. You must not include the provided Input Text as an option. 
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations.
(3) All options have both the "Passage" and "Question" components that the original Input Text had.
(3) All spacing (such as '\n' and '\t') and formatting for each options must be the exact same as that of the Input Text
(4) Options are ordered;
(5) There is not any extra explanation;
(6) You follow the following ”Format” to generate options;
(7) You comply with every specific symbol and letter detail in the given Input Text; and 
(8) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
''',
"AGNews": '''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and sentence structure of the four options must exactly match every detail in the Input Text. You must not include the provided Input Text as an option. 
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations.
(3) All spacing (such as '\n' and '\t') and formatting for each options must be the exact same as that of the Input Text
(4) Options are ordered;
(5) There is not any extra explanation;
(6) You follow the following ”Format” to generate options;
(7) You comply with every specific symbol and letter detail in the given Input Text; and 
(8) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
''',
"IMDB": '''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and sentence structure of the four options must exactly match every detail in the Input Text. You must not include the provided Input Text as an option. 
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations.
(3) All spacing (such as '\n' and '\t') and formatting for each options must be the exact same as that of the Input Text
(4) Options are ordered;
(5) There is not any extra explanation;
(6) You follow the following ”Format” to generate options;
(7) You comply with every specific symbol and letter detail in the given Input Text; and 
(8) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
''',
"GSM8K": '''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and sentence structure of the four options must exactly match every detail in the Input Text. You must not include the provided Input Text as an option. 
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations.
(3) All spacing (such as '\n' and '\t') and formatting for each options must be the exact same as that of the Input Text
(4) Options are ordered;
(5) There is not any extra explanation;
(6) You follow the following ”Format” to generate options;
(7) You comply with every specific symbol and letter detail in the given Input Text; and 
(8) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
''',
"ARC-Challenge": '''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and overall structure of the four options must exactly match every detail and the structure in the Input Text. You must not include the provided Input Text as an option. Each option in the four-question quiz you generate must include both the underlying text and answer choices in the Input Text but with word-level pertubations.
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations. 
(3) Each Option must still include the main part of the text in the Input Text with word level pertubations
(4) Each option must still include all answer choices present in the Input Text with no changes
(5) No numbers or proper nouns are changed.
(6) Options are ordered;
(7) There is not any extra explanation;
(8) You comply with the following "Format" to generate options
(9) You comply with every specific symbol and letter detail in the given Input Text; and 
(10) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
''',
"BIG-Bench-Hard": '''
Instruction: Your task is to create a four-choice quiz by replacing the words in the provided ”Input Text” with their contextually relevant synonyms. The meaning and overall structure of the four options must exactly match every detail and the structure in the Input Text. You must not include the provided Input Text as an option.
You must make sure that:
(1) You generate distinct options based on the provided Input Text;
(2) The only difference between options is word-level perturbations. 
(3) If the Input Text contains only numbers and symbols with no words, then only spacing changes may me made.
(4) If the Input Text contains answer choices then these choices must be included in each option with no changes made.
(5) No numbers or proper nouns are changed.
(6) Options are ordered;
(7) There is not any extra explanation;
(8) You comply with the following "Format" to generate options
(9) You comply with every specific symbol and letter detail in the given Input Text; and 
(10) All options retain the exact label from the Input Text, if there is one.
---
Input Text:
{instance}
---
Format:
Option 1 - 

Option 2 - 

Option 3 - 

Option 4 - 
'''
}