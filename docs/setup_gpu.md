## ⚙️ Environment & Dependencies

### Hardware Used in the Experiments
 - GPU: NVIDIA RTX 4050 Laptop Version  
 - RAM: 16 GB minimum
 - Swap: 28 GB   
 - Storage: 256 GB free disk space

### Software Requirements
 - Install Miniconda: 
     ```bash
        mkdir -p ~/miniconda3
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh
        ```
 - Activate Conda:
    ```bash
        source ~/miniconda3/bin/activate
    ```
 - Initialize Conda:
    ```bash
        conda init --all
    ```
- Create ``habitat`` environment using the following command:
    ```bash
    conda env create -f config/habitat.yml
    ```
- Activate habitat:
    ```bash
    conda activate habitat
    ```


