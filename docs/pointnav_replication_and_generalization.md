# Reproducibility: PointGoal Navigation Replication and Multi-Dataset Training

This document describes the exact configuration files and paths required to reproduce the replication and multi-dataset training experiments reported in this work.

## Design Principle

The `habitat-lab` repository is included as a **git submodule and remains unmodified**.
All experiment-specific configuration files are maintained in this repository and must be copied to the appropriate locations inside the Habitat submodule before running the experiments.

This design ensures:
- Full reproducibility
- Clear separation between upstream code and experiment-specific modifications
- Compatibility with future Habitat updates

---

## Configuration Files and Target Paths

The following configuration files are provided in the `configs/` directory of this repository.
To reproduce the experiments, copy each file to its corresponding path inside the `habitat-lab` submodule.

### 1. Task Configuration (Multi-Dataset PointNav)

**Target path:**
```
habitat-lab/habitat-lab/habitat/config/benchmark/nav/pointnav/pointnav_gibson_mp3d.yaml
```


### 2. Dataset Configuration (Gibson + Matterport3D)

**Target path:**
```
habitat-lab/habitat-lab/habitat/config/habitat/dataset/pointnav/gibson_mp3d.yaml
```

### 3. PPO Baseline Configuration (Replication)

**Target path:**
```
habitat-lab/habitat-baselines/habitat_baselines/config/pointnav/ppo_pointnav.yaml
```


---

### 4. PPO Configuration (Multi-Dataset Training)

**Target path:**
```
habitat-lab/habitat-baselines/habitat_baselines/config/pointnav/ppo_pointnav_gibson_mp3d.yaml
```

## Notes

- No changes to the Habitat source code are required.
- Training and evaluation commands are executed using the standard `habitat_baselines.run` entry point.
- All reported results were obtained using these configurations under fixed computational budgets.


