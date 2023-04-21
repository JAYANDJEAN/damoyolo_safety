FROM ubuntu
ENV PATH="/root/miniconda3/bin:${PATH}"

COPY * /root

RUN set -x; buildDeps='gcc wget ffmpeg libsm6 libxext6' \
    && apt-get update \
    && apt-get install -y $buildDeps
RUN wget -O miniconda.sh "https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py37_23.1.0-1-Linux-x86_64.sh" \
    && bash miniconda.sh -b \
    && conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 cpuonly -c pytorch \
    && pip install -r /root/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && rm miniconda.sh \
    && pip cache purge \
    && conda clean -a -y \
    && apt-get clean

EXPOSE 5000
CMD ["python", "/root/app.py"]