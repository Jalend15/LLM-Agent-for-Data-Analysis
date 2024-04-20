# LLM Agent for data analyis

This repository contains ipynb notebooks of various Agent design to tackle data analysis tasks of fires dataset.


Dataset details
-
Download Dataset used - [FPA_FOD_20170508.sqlite](https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires/data)

Agent design
-
<img width="1017" alt="image" src="https://github.com/Jalend15/LLM-Agent-for-Data-Analysis/assets/43926105/b2aa904c-d2b8-41a0-8165-ec8246181140">


Python notebooks
-
* LLM for data analysis - Iterative improvement of the plan using external API.ipynb - Follows agent design shown above with addition of external api functionality
* LLM for data analysis - Iterative improvement of the plan without external tools.ipynb - Follows agent design
* LLM for data analysis - Linear chain.ipynb - Follows agent design without the loop for iterative improvement
* LLM for data analysis - Reflection with code .ipynb - Instead of improving plan using error, this code iterates between code generator and interpreter to improve code generation
* LLM for data analysis - interaction between planner and coder.ipynb - Follows design with no improvement framework
* LLM for data analysis_sql_planner.ipynb - A simple agent to generate SQL query given natural language query and connect it to a python executor
* SQL Agent.ipynb - A simple agent to generate and validate SQL query given natural language query



Folder information
-
- Questions - Covers execution details of the queries tested
- Incontextlearning - Contains examples which will be useful for prompting
- perfectprompts - Contains example prompts to help improve data analysis tasks

Relevant documents
-
[Design slides](https://docs.google.com/presentation/d/1ZKcNQFotnZWbm7ogsoCIxgunRsfYNOG12g8GKUXuBjQ/edit?usp=sharing)




