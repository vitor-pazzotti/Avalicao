#!/bin/bash

sudo apt-get update -y > /dev/null 2>&1
sudo apt-get install zip unzip -y > /dev/null 2>&1
sudo apt-get install python3 -y > /dev/null 2>&1
sudo apt-get install python3-pip -y > /dev/null 2>&1
pip3 install requests > /dev/null 2>&1
pip3 install beautifulsoup4 > /dev/null 2>&1


mkdir vitorPazzotti
mkdir vitorPazzotti/bin
mkdir vitorPazzotti/crawler_crypto
mkdir vitorPazzotti/crawler_crypto/processados
mkdir vitorPazzotti/crawler_crypto/consolidados
mkdir vitorPazzotti/crawler_crypto/consolidados/transferidos
mkdir vitorPazzotti/crawler_dolar
mkdir vitorPazzotti/crawler_dolar/transferidos
mkdir vitorPazzotti/processados_json
mkdir vitorPazzotti/processados_json/indexados

##Pasta no HDFS
# hdfs -dfs mkdir user
# hdfs -dfs mkdir vitorPazzotti
# hdfs -dfs mkdir vitorPazzotti/input
# hdfs -dfs mkdir vitorPazzotti/input/processados
# hdfs -dfs mkdir vitorPazzotti/output
# hdfs -dfs mkdir vitorPazzotti/output/transferidos

wget -c https://github.com/vitor-pazzotti/vitor_avaliacao/archive/master.zip 
unzip master.zip
rm -rf master.zip

mv vitor_avaliacao-master/CryptoCrawler.py vitorPazzotti/bin
mv vitor_avaliacao-master/dolar.py vitorPazzotti/bin
rm -rf vitor_avaliacao-master

##Crontab de execucao do arquivo Crypto e dolar
(crontab -l 2>/dev/null; echo "40 15 * * * cd $PWD && /usr/bin/python3 $PWD/vitorPazzotti/bin/CryptoCrawler.py") | crontab -
(crontab -l 2>/dev/null; echo "41 15 * * * cd $PWD && /usr/bin/python3 $PWD/vitorPazzotti/bin/CryptoCrawler.py") | crontab -
(crontab -l 2>/dev/null; echo "46 15 */1 * * mv $PWD/vitorPazzotti/crawler_crypto/*.csv $PWD/vitorPazzotti/crawler_crypto/consolidados") | crontab -
sudo chmod -R 777 $PWD/vitorPazzotti
# sudo chmod 0777 $PWD/vitorPazzotti/crawler_crypto


##Pasta no HDFS
# hdfs -dfs mkdir user
# hdfs -dfs mkdir vitorPazzotti
# hdfs -dfs mkdir vitorPazzotti/input
# hdfs -dfs mkdir vitorPazzotti/input/processados
# hdfs -dfs mkdir vitorPazzotti/output
# hdfs -dfs mkdir vitorPazzotti/output/transferidos
# (crontab -l 2>/dev/null; echo "58 14 */1 * * hdfs -dfs") | crontab -
# zip transferidos.zip $PWD/vitorPazzotti/crawler_crypto/*.csv
# cp $PWD/transferidos.zip 
# mv $PWD/transferidos.zip $PWD/vitorPazzotti/crawler_crypto/consolidados/transferidos
# mv $PWD/transferidos.zip $PWD/vitorPazzotti/crawler_crypto/processados


