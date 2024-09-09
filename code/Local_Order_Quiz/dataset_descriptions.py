

descriptions = {
"GSM8K":'''
GSM8K consists of 8.5K high quality grade school math problems created by human problem writers. We 
segmented these into 7.5K training problems and 1K test problems. These problems take between 2 and 8 steps to 
solve, and solutions primarily involve performing a sequence of elementary calculations using basic arithmetic 
operations (+ - / *) to reach the final answer. A bright middle school student should be able to solve every problem.
''',
"HumanEval" : '''
We evaluate functional correctness on a set of 164 hand- written programming problems, which we call the HumanEval dataset. Each problem includes a function sig- nature, docstring, body, and several unit tests, with an av- erage of 7.7 tests per problem. It is important for these tasks to be hand-written, since our models are trained on a large fraction of GitHub, which already contains solutions to problems from a variety of sources. For example, there are more than ten public repositories containing solutions to Codeforces problems, which make up part of the recently proposed APPS dataset (Hendrycks et al., 2021).
Programming tasks in the HumanEval dataset assess lan- guage comprehension, reasoning, algorithms, and simple mathematics. We release the HumanEval dataset so that others can evaluate functional correctness and measure the problem-solving capabilities of their models. The dataset can be found at https://www.github.com/openai/human-eval.
'''
,
"DROP" : '''
DROP is a QA dataset which tests comprehensive understanding of paragraphs. In this crowdsourced, adversarially-created, 96k question-answering benchmark, a system must resolve multiple references in a question, map them onto a paragraph, and perform discrete operations over them (such as addition, counting, or sorting).
'''
,
"BIG-Bench-Hard" : '''
BIG-Bench (Srivastava et al., 2022) is a diverse evaluation suite that focuses on tasks believed to be beyond the capabilities of current language models. Language models have already made good progress on this benchmark, with the best model in the BIG-Bench paper outperforming average reported human-rater results on 65% of the BIG-Bench tasks via few-shot prompting. But on what tasks do language models fall short of average human-rater performance, and are those tasks actually unsolvable by current language models?
''',
"GSM8K" : '''
GSM8K consists of 8.5K high quality grade school math problems created by human problem writers. We segmented these into 7.5K training problems and 1K test problems. These problems take between 2 and 8 steps to solve, and solutions primarily involve performing a sequence of elementary calculations using basic arithmetic operations (+ - / *) to reach the final answer. A bright middle school student should be able to solve every problem.
''',
"AGNews":'''We obtained the AG's corpus of news article on the web2. It contains 496,835 categorized news articles from more than 2000 news sources. We choose the 4 largest classes from this corpus to construct our dataset, using only the title and description fields. The number of training samples for each class is 30,000 and testing 1900.''',
"MMLU": '''We create a massive multitask test consisting of multiple-choice questions from various branches of knowledge. The test spans subjects in the humanities, social sciences, hard sciences, and other areas that are important for some people to learn. There are 57 tasks in total, which is also the number of Atari games (Bellemare et al., 2013). The questions in the dataset were manually collected by graduate and undergraduate students from freely available sources online. These include practice questions for tests such as the Graduate Record Examination and the United States Medical Licensing Examination. It also includes questions designed for undergraduate courses and questions designed for readers of Oxford University Press books. Some tasks cover a subject, like psychology, but at a specific level of difficulty, such as "Elementary," "High School," "College," or "Professional."''',
"IMDB": '''We constructed a collection of 50,000 reviews from IMDB, allowing no more than 30 reviews per movie. The constructed dataset contains an even number of positive and negative reviews, so randomly guessing yields 50% accuracy. Following previous work on polarity classification, we consider only highly po- larized reviews.''',
"ARC-Challenge": '''ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence.'''
}

def get_description(dataset):    
    return descriptions[dataset]