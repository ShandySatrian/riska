**Petunjuk untuk Setup Environment - Miniconda**

1. conda create --name main-ds python=3.9
2. conda activate main-ds
3. pip install -r requirements.txt
4. Pip install matplotlib
5. pip install pandas
6. pip install seaborn
7. pip install streamlit

**Setup Shell/Terminal**
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

**Run Streamlit App on Localhost**
streamlit run dashboard/dashboard.py

**else**
Saat membaca "main_df = pd.read_csv("./dashboard/main_data.csv")" streamlit dapat membaca "./dashboard/main_data.csv" kalau "main_data.csv" saja tidak terbaca dan jalan