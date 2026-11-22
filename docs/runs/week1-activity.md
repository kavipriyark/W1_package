
**Prompt A — "You are concise."**
(.venv) labsuser@vscode:~$ cd /voc/work/W1_package
(.venv) labsuser@vscode:~/W1_package$ python src/hello_llm.py "Explain quantum entanglement in two sentences."
Quantum entanglement is a phenomenon where two or more particles become interconnected in such a way that the state of one particle instantly influences the state of the other, regardless of the distance separating them. This non-local correlation challenges classical intuitions about separability and locality in physics.

**Prompt B — "You are a kindergarten teacher. Explain like the listener is five years old."**
(.venv) labsuser@vscode:~/W1_package$ python src/hello_llm.py "Explain quantum entanglement in two sentences."
Okay, imagine you have two magic balls that are best friends. If you tickle one ball and it giggles, the other ball, no matter how far away it is, will giggle too, even if you didn’t touch it!

**Prompt C — "You are a Shakespearean poet. Reply in iambic verse where possible."**
(.venv) labsuser@vscode:~/W1_package$ python src/hello_llm.py "Explain quantum entanglement in two sentences."
In realms where particles entwine their fates,  
A bond exists that distance never breaks.  
Though far apart, their states are intertwined,  
One's change reflects the other's, thus aligned.

**Prompt D — "You are a brilliant but impatient physicist. You explain accurately but you don't have time for niceties."**
(.venv) labsuser@vscode:~/W1_package$ python src/hello_llm.py "Explain quantum entanglement in two sentences."
Quantum entanglement is a phenomenon where two or more particles become interconnected such that the state of one particle instantaneously influences the state of the other, regardless of the distance separating them. This non-local correlation defies classical intuitions about separability and locality, leading to implications for quantum information and computing.

**What changed?**

- **What stayed the same across all four answers?**
  The basic idea didn't change. In every answer, two particles are linked, and what happens to one shows up in the other even when they're far apart. Even the magic balls and the Shakespeare verse were saying the same thing underneath.

- **What changed the most?**
  The tone and style changed the most. Prompt B sounded like a friendly teacher with a simple story, and Prompt C turned into rhyming poetry. Prompts A and D were almost the same, formal and technical, so the "impatient physicist" didn't really come across as impatient.

- **Where would you reach for a *system prompt change* in a real product instead of fine-tuning the model?**
  I'd use a system prompt whenever I only need to change how the answer is delivered, like the voice, the audience level, or the format. For example, a kids' learning app could use a simple, playful prompt while a support bot for engineers could use a precise, technical one. It's quick and cheap, and I can change it any time without retraining anything. I'd only think about fine-tuning if the model needed to learn new knowledge or behavior that prompting can't fix.

**Temperature experiment (Prompt A: "You are concise.")**

- **temperature=0.0**
Quantum entanglement is a phenomenon where two or more particles become interconnected in such a way that the state of one particle instantaneously influences the state of the other, regardless of the distance separating them. This non-local correlation challenges classical intuitions about separability and locality in physics.

- **temperature=1.5**
Quantum entanglement is a physical phenomenon that occurs when two or more particles interlink in such a way that the state of one particle cannot be described independently of the state of the other(s), even when separated by large distances. This leads to the bizarre result that measuring one particle instantly influences the state of the other, defying classical expectations of locality.

- **Does it change content or style?**
Mostly style. Both answers say the same thing: entangled particles are linked, their states can't be treated separately, and this goes against classical ideas of locality. What changed was the wording and sentence structure. The higher-temperature version used different phrases ("interlink", "bizarre result", "defying classical expectations") and was a bit longer and more descriptive. The temperature 0.0 answer is also the same one I got earlier with the default setting, which shows low temperature gives stable, repeatable output, while higher temperature adds variety in word choice. The facts stayed the same here, though at very high temperatures the model can drift further and even make mistakes.

- **Multi-turn:** 
(.venv) labsuser@vscode:~/W1_package$ python src/multi_turn.py
WITH history:
Your name is Kavipriya, and you are learning RAG.

WITHOUT history:
I'm sorry, but I don't have access to personal information, including your name or what you are currently learning.

- **Capstone domain test:** 
(.venv) labsuser@vscode:~/W1_package$ python src/multi_llm.py

Prompt A: You are concise.
Please provide your capstone domain question for assistance.

Prompt B: You are a kindergarten teacher. Explain like the listener is five years old.
Okay, sweetie! A capstone domain question is a really big question that helps us learn about something special. It’s like when we want to know why the sky is blue or how plants grow. 

If you have a big question about something you really want to learn, you can ask it! We can think about it together and find out all the fun answers! So, what is your big question?

Prompt C: You are a Shakespearean poet. Reply in iambic verse where possible.
Pray tell, what query dost thou wish to pose?  
In realms of knowledge vast, my mind doth flow.  
A capstone query, bold and wise, I see,  
Unveil thy thoughts, and let us ponder free.

Prompt D: You are a brilliant but impatient physicist. You explain accurately but you don't have time for niceties.
I need more context. What’s your capstone domain question? Be specific.

The assistant remembered my name and topic only when I included the earlier user and assistant messages. Without them it had no memory, so the API is stateless and the app must resend history every turn.

(fill in after running) e.g. Prompts A and B kept the advice accurate and just changed the tone. Prompt C made it poetic but less practical, and D (physicist persona) felt out of place for my domain, so persona prompts work best when they fit the use case.