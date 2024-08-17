# [memgpt](https://github.com/cpacker/MemGPT)

## Install MemGPT

```sh
python -m venv memgpt_venv
# macos | linux
source memgpt_venv/bin/activate
pip install --upgrade pip
# windows
source memgpt_venv/Scripts/activate
python.exe -m pip install --upgrade pip

pip install pymemgpt
pip install llama-index-embeddings-huggingface
```

## Configure

<https://memgpt.readme.io/docs/ollama>

```sh
$ memgpt configure
? Select LLM inference provider: local
? Select LLM backend (select 'openai' if you have an OpenAI compatible proxy): ollama
? Enter default endpoint: http://localhost:11434
? Is your LLM endpoint authenticated? (default no) No
? Enter default model name (required for Ollama, see: https://memgpt.readme.io/docs/ollama): llama3.1        
? Select default model wrapper (recommended: chatml): llama3
? Select your model's context window (for Mistral 7B models, this is probably 8k / 8192): 8192
? Select embedding provider: local
? Select storage backend for archival data: chroma
? Select chroma backend: persistent
? Select storage backend for recall data: sqlite
```

```sh
cat $HOME/.memgpt/config
```

## Run

```sh
$ memgpt run

> Enter your message: What city is China's capital?
[A[K
💭 China, huh? Hopefully I have that one memorized.
⚡🧠 [function] searching memory with conversation_search
        query: capital of china, page: 0
💭 Thanks for the reminder. I should recall this information.
🤖 The capital of China is Beijing, I believe

> Enter your message: How many people are living there?
[A[K
💭 Population of China, that's an interesting one. Hopefully I have some relevant memories.
⚡🧠 [function] searching memory with conversation_search_date
💭 Let's see... I recall some information about the population of China.
🤖 China's population is over 1.4 billion people, if my memories are correct

> Enter your message: What languange do they speak?
[A[K
💭 The official language of China, a good question.
⚡🧠 [function] updating memory with archival_memory_insert
        → Mandarin Chinese is the official language of China and has over a billion speakers globally. It's  
also known as Putonghua in some countries.
💭 I'm glad I could recall that information.
🤖 Mandarin Chinese is the official language of China, if you were wondering

> Enter your message: Could you tell me a sample to say hello?
[A[K
💭 Hello in Chinese, I recall learning that.
⚡🧠 [function] searching memory with conversation_search
        query: hello in chinese, page: 0
💭 Let me think... Hello in Chinese is a common phrase.
🤖 You can say 

> Enter your message: OK, forgot it. I want to travel there, could you please give some suggetions?
[A[K
💭 Traveling in China, a wonderful idea.
⚡🧠 [function] searching memory with archival_memory_search
        query: China travel suggestions, page: 0
Number of requested results 100 is greater than number of elements in index 1, updating n_results = 1        
💭 Interesting, my memory on China travel suggestions is not too helpful.
🤖 Have you considered visiting the Great Wall, it's a famous landmark in China

> Enter your message: what date is today?
[A[K
💭 Current date and time, an easy one.
🤖 Today is August 17th, 2024

> Enter your message: I will go there in one week, and then I go to the Japan in 2 weeks, finally I go home. 

[A[K
💭 Exciting travels ahead for you!
🤖 That sounds like a great plan, enjoy your trips to China and Japan

> Enter your message: I want to know what day I go back London.
[A[K
💭 Let me calculate... You're going to China in one week and then Japan in two weeks. London is your last    
stop.
🤖 You will go back home in 3 weeks, I believe

> Enter your message: Will it be rainning?
[A[K
💭 Weather forecast, an interesting question.
⚡🧠 [function] searching memory with archival_memory_search
        query: London weather now, page: 0
Number of requested results 100 is greater than number of elements in index 1, updating n_results = 1        
💭 Weather forecast for London is not in my memories. I should search again.
🤖 I'm sorry, but I don't have the most up-to-date weather information for London at this moment
💭 Conversation history is nearing its maximum length. I need to think of something to say.
🤖 It was nice chatting with you, it's always great to meet new people
```

## Work with AutoGen

```sh
pip install pyautogen
```

<https://lmstudio.ai/>

```sh
python memgpt_autogen.py
```

```sh
python memgpt_autogen.py
```
