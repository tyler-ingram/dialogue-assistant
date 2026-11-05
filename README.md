# dialogue-assistant
A agent for helping generate dialogue between characters.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Environment Configuration](#environment-configuration)

---

## Overview

TODO
---

## Prerequisites

- Python 3.13+
- React
- [`uv`](https://docs.astral.sh/uv/) for dependency management
- Install LM Studio [from https://lmstudio.ai/](https://lmstudio.ai/docs/developer/core/headless)

---

## Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/tyler-ingram/dialogue-assisstant
cd backend
uv sync
lms get qwen/qwen3-4b-2507

```

To get another model:
```bash
lms get <model_name>
```
---

## Environment Configuration

Copy the example env file:

```bash
cp .env.example .env
```
If a different model is chosen during setup, ensure that the .env file states which model you want to use in the LM_MODEL field.

## Running the code
To start the lms server to query models
```bash
#In the backend
lms daemon up
lms server start
```
---