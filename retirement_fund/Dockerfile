FROM eboraas/jupyter:standard

# docker build -t minipro .
# docker run --rm -d -v $(pwd)/retirement_fund:/mnt/notebooks/ -p 8888:8888 minipro
RUN apt-get update
RUN apt-get install -y locales locales-all
RUN locale-gen es_ES.UTF-8
RUN pip install --no-cache-dir pandas==0.20.2 requests==2.18.1
EXPOSE 8888

CMD ["/bin/sh", "-c", "/usr/local/bin/jupyter-notebook --no-browser --ip=0.0.0.0 --notebook-dir=/mnt/notebooks"]

