FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip install pandas --user
RUN pip install numpy --user
RUN pip install matplotlib --user
# RUN pip install seaborn --user
RUN pip install scikit-learn --user
# RUN pip install scipy --user


RUN mkdir /home/doc-bd-a1/

COPY dataset.csv /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/
COPY load.py /home/doc-bd-a1/
COPY model.py /home/doc-bd-a1/
COPY vis.py /home/doc-bd-a1/
COPY final.sh /home/doc-bd-a1/

CMD ["bash"]