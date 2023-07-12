FROM --platform=linux/amd64 continuumio/miniconda3

RUN mkdir -p /backend
COPY ./backend /backend

RUN /opt/conda/bin/conda env create -f /backend/requirements.yml
ENV PATH /opt/conda/envs/luna/bin:$PATH
RUN echo "source activate luna"> ~/.bashrc

WORKDIR /backend
