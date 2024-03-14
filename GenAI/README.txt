Generative AI and LLM Work

1. LLM on single data set with agent

- Goal: to connect a LLM with a specific data set and be able to query with an agent to understand content.
- Components: OpenAI (LLM) + LlamaIndex + LangChain

2. LLM with AI-in-the-loop

<a target="_blank" href="https://colab.research.google.com/github/fdletter1980/fdletter1980.github.io/blob/main/GenAI/LLM%20RAG%20with%20AI-in-the-loop/LLM%20RAG%20with%20AI-in-the-loop.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

- Goal: to evolve LLM use case to encapsulate key elements for Responsible AI and UX in order to have out-of-the-bop LLM Ops Monitoring along with key metrics to assess accuracy of the response and data lineage. 
- Approach: augmenting Human-in-the-loop with AI-in-the-loop. Example colab covers a conversational agent with RAG and memory persistence using GPT 3.5 Turbo and streaming responses were evaluated by Bison. Completely templatized so you can switch in and out any foundational LLM.
- Components: OpenAI & Bison (can be any LLM) + RAG + Vector DB + LangChain + Arize
