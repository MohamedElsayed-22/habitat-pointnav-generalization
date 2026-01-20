
# 📘 **Analyzing Generalization in Habitat PointGoal Navigation**

## 🧭 Overview
This repository contains a replication and analysis of the **Depth-based PPO PointGoal Navigation (PointNav)** agent from the Habitat framework.  
The goal is to study **generalization to unseen environments** under the original Habitat evaluation protocol, with a focus on controlled experiments under limited compute.



## 📄 Abstract
This repository presents a faithful replication of the Depth-based PPO agent for PointGoal Navigation introduced in the Habitat framework.  
Core trends reported in prior work are reproduced in this repo, including the generalization gap between seen and unseen environments, using **Gibson** and **Matterport3D** datasets.

- All experiments are conducted under constrained compute to emphasize controlled analysis rather than large-scale training.  
- This repository also serves as a foundation for lightweight generalization-oriented extensions explored in subsequent work.


## 🎯 Research Objectives
- Replicate the Depth-based PPO PointNav baseline under the original Habitat evaluation protocol.
- Verify generalization behavior when evaluated on unseen environments.
- Quantify the performance gap between in-domain and cross-dataset evaluation.
- Establish a clean experimental baseline for future generalization-oriented extensions.

## 🧠 Baseline Method (Habitat PPO-Depth)
The baseline agent follows the standard Habitat PPO PointNav setup with **Depth-only observations**.

Key components:
- Proximal Policy Optimization (PPO)
- Depth visual input
- Continuous navigation actions
- SPL-based evaluation on unseen environments

All architectural and training details follow the official Habitat baselines implementation.


## 📂 Dataset / Data Collection
The experiments use standard Habitat navigation datasets:

- **Gibson**: Used for training
- **Matterport3D (MP3D)**: Used for cross-dataset evaluation

Both datasets are used with the official Habitat splits to ensure comparability with prior work.
 

<!-- 📁 **Example directory structure:** -->

<!-- >_Example:_
```Datasets/
└── {dataset_name}/
├── train/
│   ├── images/
│   └── labels/
├── validate/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

>_Example:_
>- Images _(samples in general)_ must be `{format}`  
>- Labels must be `{format}` and match filenames of corresponding images

## 🧼 Preprocessing & Augmentation
Explain all preprocessing steps and optional data augmentation applied to the dataset. -->

<!-- ### Preprocessing Steps
>_Example:_
>- Resize images to a fixed resolution without distortion  
>- Apply centered padding  
>- Transpose or flip images if required for dataset consistency  

📌 *Insert preprocessing diagram below:*  
`![Figure X: Preprocessing Steps](path/to/preprocessing_steps.png)`  
**Figure X:** Caption describing preprocessing steps


### Label Encoding
- Encode labels using `{encoding_method}`  
- Use `{padding_token}` for fixed-length padding if required -->

## 🌳 Project Structure
```text
pointnav-generalization/
├── habitat-lab/          # Habitat submodule 
├── configs/              # Experiment configs
├── results/              # Logs, checkpoints, plots
├── notes/                # Replication log and observations
├── docs/                 # guide to implementations
├── LICENSE               
└── README.md
```


## 🏋️ Training Instructions


### Setup
1. Install dependencies:
    
    Please follow the environment setup instructions in `docs/`.

***to be further elaborated***

<!-- 2. Training: -->
<!-- ```bash
python train.py --arg1 value1 --arg2 value2
``` -->

<!-- ### Key Training Details

- Batch size: `{batch_size}`
- Learning rate: `{learning_rate}`
- Number of epochs: `{num_epochs}`
- Checkpointing: Save best model as `{checkpoint_name}`
- Early stopping criteria: `{criteria}`
- Optional callbacks: `{callback_names}` -->

<!-- ## 🧪 Evaluation
Describe how to evaluate the trained model and what metrics are reported.

### Evaluation Command
```bash
python evaluate.py --model {checkpoint_path} --data {dataset_path}
```
### Metrics Computed
>_Example_
>- Per-sample predictions
>- Character-level accuracy
>- Global accuracy / overall score
>- Precision, Recall, F1-score (if applicable)
>- Loss curves -->

<!-- ### Inspecting Outputs
>_Example_
>- Decoded outputs for selected samples are saved to `{output_folder}`.   
>-Visualizations can be generated for qualitative analysis. -->

<!-- ## 📊 Results & Discussion
Summarize the findings of your experiments, including quantitative and qualitative results. -->

<!-- ### Quantitative Results
> _Example_
>| Experiment | Metric 1 | Metric 2 | Notes |
>|------------|----------|----------|-------|
>| Baseline   | 0.85     | 0.78     | -     |
>| Proposed   | 0.92     | 0.88     | Improved with attention mechanism |

### Qualitative Results
- Show example outputs for key samples  
- Compare predictions with ground truth  
- Highlight common errors or patterns

### Discussion
- Interpret results and explain trends  
- Compare with prior work if relevant  
- Mention limitations observed in the results -->

<!-- ## ⚙️ Environment & Dependencies
List all dependencies, hardware/software requirements, and setup instructions to reproduce the experiments.

### Hardware Requirements
> _Example:_  
> - GPU: NVIDIA RTX 3090 or equivalent  
> - RAM: 32 GB minimum  
> - Storage: 100 GB free disk space

### Software Requirements
> _Example:_  
> - Python 3.10  
> - CUDA 11.8 (if using GPU)  
> - Operating System: Ubuntu 22.04 / Windows 11

### Python Dependencies

>_Example:_  
Install all required packages using pip:

```bash
pip install -r requirements.txt
```

>_Example:_  
create Python environment using conda:

```bash
conda env create -f env.yml
conda activate env
```

### Optional Tools
>_Example:_
>- Jupyter Notebook / Jupyter Lab for interactive exploration
>- Visual Studio Code or PyCharm for development
>- Git LFS for large datasets -->



## 📄 License
This repository is licensed under the MIT License. See the [MIT License](LICENSE) file for more details.


## 🙌 Acknowledgements
- This README structure was inspired by the Research README template from
[MohamedElsayed-22/README-templates](https://github.com/MohamedElsayed-22/README-templates).
 - The developers of [facebookresearch/habitat-lab](https://github.com/facebookresearch/habitat-lab) are appreciated for their open-source contributions.  
