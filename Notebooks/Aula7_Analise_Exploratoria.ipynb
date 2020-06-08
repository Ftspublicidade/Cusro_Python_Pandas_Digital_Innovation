{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Aula8-Analise_Exploratoria.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "G5HpRApza9UR",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Importando as bibliotecas\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "plt.style.use(\"seaborn\")"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3qLVp0Z_bUXq",
        "colab_type": "code",
        "outputId": "0aff5a55-7dc4-495b-c217-0c15f8750e35",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7Ci8vIE1heCBhbW91bnQgb2YgdGltZSB0byBibG9jayB3YWl0aW5nIGZvciB0aGUgdXNlci4KY29uc3QgRklMRV9DSEFOR0VfVElNRU9VVF9NUyA9IDMwICogMTAwMDsKCmZ1bmN0aW9uIF91cGxvYWRGaWxlcyhpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IHN0ZXBzID0gdXBsb2FkRmlsZXNTdGVwKGlucHV0SWQsIG91dHB1dElkKTsKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIC8vIENhY2hlIHN0ZXBzIG9uIHRoZSBvdXRwdXRFbGVtZW50IHRvIG1ha2UgaXQgYXZhaWxhYmxlIGZvciB0aGUgbmV4dCBjYWxsCiAgLy8gdG8gdXBsb2FkRmlsZXNDb250aW51ZSBmcm9tIFB5dGhvbi4KICBvdXRwdXRFbGVtZW50LnN0ZXBzID0gc3RlcHM7CgogIHJldHVybiBfdXBsb2FkRmlsZXNDb250aW51ZShvdXRwdXRJZCk7Cn0KCi8vIFRoaXMgaXMgcm91Z2hseSBhbiBhc3luYyBnZW5lcmF0b3IgKG5vdCBzdXBwb3J0ZWQgaW4gdGhlIGJyb3dzZXIgeWV0KSwKLy8gd2hlcmUgdGhlcmUgYXJlIG11bHRpcGxlIGFzeW5jaHJvbm91cyBzdGVwcyBhbmQgdGhlIFB5dGhvbiBzaWRlIGlzIGdvaW5nCi8vIHRvIHBvbGwgZm9yIGNvbXBsZXRpb24gb2YgZWFjaCBzdGVwLgovLyBUaGlzIHVzZXMgYSBQcm9taXNlIHRvIGJsb2NrIHRoZSBweXRob24gc2lkZSBvbiBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcCwKLy8gdGhlbiBwYXNzZXMgdGhlIHJlc3VsdCBvZiB0aGUgcHJldmlvdXMgc3RlcCBhcyB0aGUgaW5wdXQgdG8gdGhlIG5leHQgc3RlcC4KZnVuY3Rpb24gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpIHsKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIGNvbnN0IHN0ZXBzID0gb3V0cHV0RWxlbWVudC5zdGVwczsKCiAgY29uc3QgbmV4dCA9IHN0ZXBzLm5leHQob3V0cHV0RWxlbWVudC5sYXN0UHJvbWlzZVZhbHVlKTsKICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKG5leHQudmFsdWUucHJvbWlzZSkudGhlbigodmFsdWUpID0+IHsKICAgIC8vIENhY2hlIHRoZSBsYXN0IHByb21pc2UgdmFsdWUgdG8gbWFrZSBpdCBhdmFpbGFibGUgdG8gdGhlIG5leHQKICAgIC8vIHN0ZXAgb2YgdGhlIGdlbmVyYXRvci4KICAgIG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSA9IHZhbHVlOwogICAgcmV0dXJuIG5leHQudmFsdWUucmVzcG9uc2U7CiAgfSk7Cn0KCi8qKgogKiBHZW5lcmF0b3IgZnVuY3Rpb24gd2hpY2ggaXMgY2FsbGVkIGJldHdlZW4gZWFjaCBhc3luYyBzdGVwIG9mIHRoZSB1cGxvYWQKICogcHJvY2Vzcy4KICogQHBhcmFtIHtzdHJpbmd9IGlucHV0SWQgRWxlbWVudCBJRCBvZiB0aGUgaW5wdXQgZmlsZSBwaWNrZXIgZWxlbWVudC4KICogQHBhcmFtIHtzdHJpbmd9IG91dHB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIG91dHB1dCBkaXNwbGF5LgogKiBAcmV0dXJuIHshSXRlcmFibGU8IU9iamVjdD59IEl0ZXJhYmxlIG9mIG5leHQgc3RlcHMuCiAqLwpmdW5jdGlvbiogdXBsb2FkRmlsZXNTdGVwKGlucHV0SWQsIG91dHB1dElkKSB7CiAgY29uc3QgaW5wdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoaW5wdXRJZCk7CiAgaW5wdXRFbGVtZW50LmRpc2FibGVkID0gZmFsc2U7CgogIGNvbnN0IG91dHB1dEVsZW1lbnQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChvdXRwdXRJZCk7CiAgb3V0cHV0RWxlbWVudC5pbm5lckhUTUwgPSAnJzsKCiAgY29uc3QgcGlja2VkUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICBpbnB1dEVsZW1lbnQuYWRkRXZlbnRMaXN0ZW5lcignY2hhbmdlJywgKGUpID0+IHsKICAgICAgcmVzb2x2ZShlLnRhcmdldC5maWxlcyk7CiAgICB9KTsKICB9KTsKCiAgY29uc3QgY2FuY2VsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnYnV0dG9uJyk7CiAgaW5wdXRFbGVtZW50LnBhcmVudEVsZW1lbnQuYXBwZW5kQ2hpbGQoY2FuY2VsKTsKICBjYW5jZWwudGV4dENvbnRlbnQgPSAnQ2FuY2VsIHVwbG9hZCc7CiAgY29uc3QgY2FuY2VsUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICBjYW5jZWwub25jbGljayA9ICgpID0+IHsKICAgICAgcmVzb2x2ZShudWxsKTsKICAgIH07CiAgfSk7CgogIC8vIENhbmNlbCB1cGxvYWQgaWYgdXNlciBoYXNuJ3QgcGlja2VkIGFueXRoaW5nIGluIHRpbWVvdXQuCiAgY29uc3QgdGltZW91dFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgc2V0VGltZW91dCgoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9LCBGSUxFX0NIQU5HRV9USU1FT1VUX01TKTsKICB9KTsKCiAgLy8gV2FpdCBmb3IgdGhlIHVzZXIgdG8gcGljayB0aGUgZmlsZXMuCiAgY29uc3QgZmlsZXMgPSB5aWVsZCB7CiAgICBwcm9taXNlOiBQcm9taXNlLnJhY2UoW3BpY2tlZFByb21pc2UsIHRpbWVvdXRQcm9taXNlLCBjYW5jZWxQcm9taXNlXSksCiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdzdGFydGluZycsCiAgICB9CiAgfTsKCiAgaWYgKCFmaWxlcykgewogICAgcmV0dXJuIHsKICAgICAgcmVzcG9uc2U6IHsKICAgICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICAgIH0KICAgIH07CiAgfQoKICBjYW5jZWwucmVtb3ZlKCk7CgogIC8vIERpc2FibGUgdGhlIGlucHV0IGVsZW1lbnQgc2luY2UgZnVydGhlciBwaWNrcyBhcmUgbm90IGFsbG93ZWQuCiAgaW5wdXRFbGVtZW50LmRpc2FibGVkID0gdHJ1ZTsKCiAgZm9yIChjb25zdCBmaWxlIG9mIGZpbGVzKSB7CiAgICBjb25zdCBsaSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2xpJyk7CiAgICBsaS5hcHBlbmQoc3BhbihmaWxlLm5hbWUsIHtmb250V2VpZ2h0OiAnYm9sZCd9KSk7CiAgICBsaS5hcHBlbmQoc3BhbigKICAgICAgICBgKCR7ZmlsZS50eXBlIHx8ICduL2EnfSkgLSAke2ZpbGUuc2l6ZX0gYnl0ZXMsIGAgKwogICAgICAgIGBsYXN0IG1vZGlmaWVkOiAkewogICAgICAgICAgICBmaWxlLmxhc3RNb2RpZmllZERhdGUgPyBmaWxlLmxhc3RNb2RpZmllZERhdGUudG9Mb2NhbGVEYXRlU3RyaW5nKCkgOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbi9hJ30gLSBgKSk7CiAgICBjb25zdCBwZXJjZW50ID0gc3BhbignMCUgZG9uZScpOwogICAgbGkuYXBwZW5kQ2hpbGQocGVyY2VudCk7CgogICAgb3V0cHV0RWxlbWVudC5hcHBlbmRDaGlsZChsaSk7CgogICAgY29uc3QgZmlsZURhdGFQcm9taXNlID0gbmV3IFByb21pc2UoKHJlc29sdmUpID0+IHsKICAgICAgY29uc3QgcmVhZGVyID0gbmV3IEZpbGVSZWFkZXIoKTsKICAgICAgcmVhZGVyLm9ubG9hZCA9IChlKSA9PiB7CiAgICAgICAgcmVzb2x2ZShlLnRhcmdldC5yZXN1bHQpOwogICAgICB9OwogICAgICByZWFkZXIucmVhZEFzQXJyYXlCdWZmZXIoZmlsZSk7CiAgICB9KTsKICAgIC8vIFdhaXQgZm9yIHRoZSBkYXRhIHRvIGJlIHJlYWR5LgogICAgbGV0IGZpbGVEYXRhID0geWllbGQgewogICAgICBwcm9taXNlOiBmaWxlRGF0YVByb21pc2UsCiAgICAgIHJlc3BvbnNlOiB7CiAgICAgICAgYWN0aW9uOiAnY29udGludWUnLAogICAgICB9CiAgICB9OwoKICAgIC8vIFVzZSBhIGNodW5rZWQgc2VuZGluZyB0byBhdm9pZCBtZXNzYWdlIHNpemUgbGltaXRzLiBTZWUgYi82MjExNTY2MC4KICAgIGxldCBwb3NpdGlvbiA9IDA7CiAgICB3aGlsZSAocG9zaXRpb24gPCBmaWxlRGF0YS5ieXRlTGVuZ3RoKSB7CiAgICAgIGNvbnN0IGxlbmd0aCA9IE1hdGgubWluKGZpbGVEYXRhLmJ5dGVMZW5ndGggLSBwb3NpdGlvbiwgTUFYX1BBWUxPQURfU0laRSk7CiAgICAgIGNvbnN0IGNodW5rID0gbmV3IFVpbnQ4QXJyYXkoZmlsZURhdGEsIHBvc2l0aW9uLCBsZW5ndGgpOwogICAgICBwb3NpdGlvbiArPSBsZW5ndGg7CgogICAgICBjb25zdCBiYXNlNjQgPSBidG9hKFN0cmluZy5mcm9tQ2hhckNvZGUuYXBwbHkobnVsbCwgY2h1bmspKTsKICAgICAgeWllbGQgewogICAgICAgIHJlc3BvbnNlOiB7CiAgICAgICAgICBhY3Rpb246ICdhcHBlbmQnLAogICAgICAgICAgZmlsZTogZmlsZS5uYW1lLAogICAgICAgICAgZGF0YTogYmFzZTY0LAogICAgICAgIH0sCiAgICAgIH07CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPQogICAgICAgICAgYCR7TWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCl9JSBkb25lYDsKICAgIH0KICB9CgogIC8vIEFsbCBkb25lLgogIHlpZWxkIHsKICAgIHJlc3BvbnNlOiB7CiAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgIH0KICB9Owp9CgpzY29wZS5nb29nbGUgPSBzY29wZS5nb29nbGUgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYiA9IHNjb3BlLmdvb2dsZS5jb2xhYiB8fCB7fTsKc2NvcGUuZ29vZ2xlLmNvbGFiLl9maWxlcyA9IHsKICBfdXBsb2FkRmlsZXMsCiAgX3VwbG9hZEZpbGVzQ29udGludWUsCn07Cn0pKHNlbGYpOwo=",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 74
        }
      },
      "source": [
        "#Upload do arquivo\n",
        "from google.colab import files\n",
        "arq = files.upload()"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-a8fe5d14-f053-4b7d-98eb-b5ad1d50c22f\" name=\"files[]\" multiple disabled />\n",
              "     <output id=\"result-a8fe5d14-f053-4b7d-98eb-b5ad1d50c22f\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "Saving AdventureWorks.xlsx to AdventureWorks (5).xlsx\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Rpxs2yU0ba23",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Criando nosso DataFrame\n",
        "df = pd.read_excel(\"AdventureWorks.xlsx\")"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DPOEg0MikIXG",
        "colab_type": "code",
        "outputId": "633ff3c2-2339-4b86-8110-b65b6d29e2d2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        }
      },
      "source": [
        "#Visualizando as 5 primeiras linhas\n",
        "df.head()"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Data Envio</th>\n",
              "      <th>ID Loja</th>\n",
              "      <th>ID Produto</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>No. Venda</th>\n",
              "      <th>Custo Unitário</th>\n",
              "      <th>Preço Unitário</th>\n",
              "      <th>Quantidade</th>\n",
              "      <th>Valor Desconto</th>\n",
              "      <th>Valor Venda</th>\n",
              "      <th>Produto</th>\n",
              "      <th>Fabricante</th>\n",
              "      <th>Marca</th>\n",
              "      <th>Classe</th>\n",
              "      <th>Cor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2008-05-09</td>\n",
              "      <td>2008-05-29</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18839</td>\n",
              "      <td>200805093CS607</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2008-05-12</td>\n",
              "      <td>2008-05-17</td>\n",
              "      <td>306</td>\n",
              "      <td>384</td>\n",
              "      <td>19051</td>\n",
              "      <td>200805123CS567</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2008-05-14</td>\n",
              "      <td>2008-05-20</td>\n",
              "      <td>306</td>\n",
              "      <td>384</td>\n",
              "      <td>19052</td>\n",
              "      <td>200805143CS576</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2008-05-21</td>\n",
              "      <td>2008-05-27</td>\n",
              "      <td>306</td>\n",
              "      <td>384</td>\n",
              "      <td>19052</td>\n",
              "      <td>200805213CS576</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2008-06-20</td>\n",
              "      <td>2008-06-27</td>\n",
              "      <td>306</td>\n",
              "      <td>384</td>\n",
              "      <td>19053</td>\n",
              "      <td>200806203CS586</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Data Venda Data Envio  ID Loja  ...            Marca   Classe  Cor\n",
              "0 2008-05-09 2008-05-29      199  ...  Adventure Works  Regular  Red\n",
              "1 2008-05-12 2008-05-17      306  ...  Adventure Works  Regular  Red\n",
              "2 2008-05-14 2008-05-20      306  ...  Adventure Works  Regular  Red\n",
              "3 2008-05-21 2008-05-27      306  ...  Adventure Works  Regular  Red\n",
              "4 2008-06-20 2008-06-27      306  ...  Adventure Works  Regular  Red\n",
              "\n",
              "[5 rows x 16 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UCJpu--kK9wo",
        "colab_type": "code",
        "outputId": "8d55d823-0742-4a54-fcb2-16df652007da",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#Quantidade de linhas e colunas\n",
        "df.shape"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(904, 16)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "P9S1i8o1lUu-",
        "colab_type": "code",
        "outputId": "6197dad1-cbfe-444a-a212-1bfa12541ebd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 306
        }
      },
      "source": [
        "#Verificando os tipos de dados\n",
        "df.dtypes"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Data Venda        datetime64[ns]\n",
              "Data Envio        datetime64[ns]\n",
              "ID Loja                    int64\n",
              "ID Produto                 int64\n",
              "ID Cliente                 int64\n",
              "No. Venda                 object\n",
              "Custo Unitário           float64\n",
              "Preço Unitário           float64\n",
              "Quantidade                 int64\n",
              "Valor Desconto           float64\n",
              "Valor Venda              float64\n",
              "Produto                   object\n",
              "Fabricante                object\n",
              "Marca                     object\n",
              "Classe                    object\n",
              "Cor                       object\n",
              "dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "duheNX1GlhWw",
        "colab_type": "code",
        "outputId": "0b047796-3ab7-4dd4-a370-ecce8e256679",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#Qual a Receita total?\n",
        "df[\"Valor Venda\"].sum()"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5984606.1426"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IHop-35BlyDO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Qual o custo Total?\n",
        "df[\"custo\"] = df[\"Custo Unitário\"].mul(df[\"Quantidade\"]) #Criando a coluna de custo"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3fy4QmNLmMWd",
        "colab_type": "code",
        "outputId": "b08296d5-566d-4123-a8d7-b2c4d959e935",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        }
      },
      "source": [
        "df.head(1)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Data Envio</th>\n",
              "      <th>ID Loja</th>\n",
              "      <th>ID Produto</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>No. Venda</th>\n",
              "      <th>Custo Unitário</th>\n",
              "      <th>Preço Unitário</th>\n",
              "      <th>Quantidade</th>\n",
              "      <th>Valor Desconto</th>\n",
              "      <th>Valor Venda</th>\n",
              "      <th>Produto</th>\n",
              "      <th>Fabricante</th>\n",
              "      <th>Marca</th>\n",
              "      <th>Classe</th>\n",
              "      <th>Cor</th>\n",
              "      <th>custo</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2008-05-09</td>\n",
              "      <td>2008-05-29</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18839</td>\n",
              "      <td>200805093CS607</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2091.48</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Data Venda Data Envio  ID Loja  ...   Classe  Cor    custo\n",
              "0 2008-05-09 2008-05-29      199  ...  Regular  Red  2091.48\n",
              "\n",
              "[1 rows x 17 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Uj7LTfyumqcn",
        "colab_type": "code",
        "outputId": "ed0c7864-fc3c-40e2-e2e1-04182d758866",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#Qual o custo Total?\n",
        "round(df[\"custo\"].sum(), 2)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2486783.05"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dcL7yq6dm6-R",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Agora que temos a receita e custo e o total, podemos achar o Lucro total\n",
        "#Vamos criar uma coluna de Lucro que será Receita - Custo\n",
        "df[\"lucro\"]  = df[\"Valor Venda\"] - df[\"custo\"] "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AESBzwFuqgy4",
        "colab_type": "code",
        "outputId": "a832d8aa-bbee-41c6-e823-5844dd61890c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        }
      },
      "source": [
        "df.head(1)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Data Envio</th>\n",
              "      <th>ID Loja</th>\n",
              "      <th>ID Produto</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>No. Venda</th>\n",
              "      <th>Custo Unitário</th>\n",
              "      <th>Preço Unitário</th>\n",
              "      <th>Quantidade</th>\n",
              "      <th>Valor Desconto</th>\n",
              "      <th>Valor Venda</th>\n",
              "      <th>Produto</th>\n",
              "      <th>Fabricante</th>\n",
              "      <th>Marca</th>\n",
              "      <th>Classe</th>\n",
              "      <th>Cor</th>\n",
              "      <th>custo</th>\n",
              "      <th>lucro</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2008-05-09</td>\n",
              "      <td>2008-05-29</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18839</td>\n",
              "      <td>200805093CS607</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2091.48</td>\n",
              "      <td>2456.52</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Data Venda Data Envio  ID Loja  ID Produto  ...   Classe  Cor    custo    lucro\n",
              "0 2008-05-09 2008-05-29      199         384  ...  Regular  Red  2091.48  2456.52\n",
              "\n",
              "[1 rows x 18 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "odfh78ayqpN4",
        "colab_type": "code",
        "outputId": "8e29504f-0eb5-4bc7-8312-ae1df3d7de5f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#Total Lucro\n",
        "round(df[\"lucro\"].sum(),2)"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3497823.09"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dOlaVDsFqv-t",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Criando uma coluna com total de dias para enviar o produto\n",
        "df[\"Tempo_envio\"] = df[\"Data Envio\"] - df[\"Data Venda\"]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xzf6mIH5r3vy",
        "colab_type": "code",
        "outputId": "e5444795-08c5-434f-b88a-0043c6fb2c66",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        }
      },
      "source": [
        "df.head(1)"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Data Envio</th>\n",
              "      <th>ID Loja</th>\n",
              "      <th>ID Produto</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>No. Venda</th>\n",
              "      <th>Custo Unitário</th>\n",
              "      <th>Preço Unitário</th>\n",
              "      <th>Quantidade</th>\n",
              "      <th>Valor Desconto</th>\n",
              "      <th>Valor Venda</th>\n",
              "      <th>Produto</th>\n",
              "      <th>Fabricante</th>\n",
              "      <th>Marca</th>\n",
              "      <th>Classe</th>\n",
              "      <th>Cor</th>\n",
              "      <th>custo</th>\n",
              "      <th>lucro</th>\n",
              "      <th>Tempo_envio</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2008-05-09</td>\n",
              "      <td>2008-05-29</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18839</td>\n",
              "      <td>200805093CS607</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2091.48</td>\n",
              "      <td>2456.52</td>\n",
              "      <td>20 days</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Data Venda Data Envio  ID Loja  ID Produto  ...  Cor    custo    lucro  Tempo_envio\n",
              "0 2008-05-09 2008-05-29      199         384  ...  Red  2091.48  2456.52      20 days\n",
              "\n",
              "[1 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tYKqnysZthDh",
        "colab_type": "text"
      },
      "source": [
        "**Agora, queremos saber a média do tempo de envio para cada Marca, e para isso precisamos transformar a coluna Tempo_envio em númerica**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eUAJwu45uVV-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Extraindo apenas os dias\n",
        "df[\"Tempo_envio\"] = (df[\"Data Envio\"] - df[\"Data Venda\"]).dt.days"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MngNW5dZxjh_",
        "colab_type": "code",
        "outputId": "ce20f74d-8730-463e-ed5e-b0a40104bcd7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        }
      },
      "source": [
        "df.head(1)"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Data Envio</th>\n",
              "      <th>ID Loja</th>\n",
              "      <th>ID Produto</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>No. Venda</th>\n",
              "      <th>Custo Unitário</th>\n",
              "      <th>Preço Unitário</th>\n",
              "      <th>Quantidade</th>\n",
              "      <th>Valor Desconto</th>\n",
              "      <th>Valor Venda</th>\n",
              "      <th>Produto</th>\n",
              "      <th>Fabricante</th>\n",
              "      <th>Marca</th>\n",
              "      <th>Classe</th>\n",
              "      <th>Cor</th>\n",
              "      <th>custo</th>\n",
              "      <th>lucro</th>\n",
              "      <th>Tempo_envio</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2008-05-09</td>\n",
              "      <td>2008-05-29</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18839</td>\n",
              "      <td>200805093CS607</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.0</td>\n",
              "      <td>6</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4548.0</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2091.48</td>\n",
              "      <td>2456.52</td>\n",
              "      <td>20</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Data Venda Data Envio  ID Loja  ...    custo    lucro Tempo_envio\n",
              "0 2008-05-09 2008-05-29      199  ...  2091.48  2456.52          20\n",
              "\n",
              "[1 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k9le4YEvxlow",
        "colab_type": "code",
        "outputId": "4fa5b1a9-e7c4-43ba-f074-7e539c3faf8e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#Verificando o tipo da coluna Tempo_envio\n",
        "df[\"Tempo_envio\"].dtype"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dtype('int64')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VtCqhtr60byy",
        "colab_type": "code",
        "outputId": "8f08f2ff-50b9-40c3-b103-153a19a4e335",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 102
        }
      },
      "source": [
        "#Média do tempo de envio por Marca\n",
        "df.groupby(\"Marca\")[\"Tempo_envio\"].mean()"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Marca\n",
              "Adventure Works    8.663866\n",
              "Contoso            8.470930\n",
              "Fabrikam           8.510121\n",
              "Name: Tempo_envio, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "I1sg7kwKjuU1",
        "colab_type": "text"
      },
      "source": [
        " **Missing Values**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a26UV-kTjmog",
        "colab_type": "code",
        "outputId": "2db6fd94-9426-4085-c484-81ac68e32e6c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "#Verificando se temos dados faltantes\n",
        "df.isnull().sum()"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Data Venda        0\n",
              "Data Envio        0\n",
              "ID Loja           0\n",
              "ID Produto        0\n",
              "ID Cliente        0\n",
              "No. Venda         0\n",
              "Custo Unitário    0\n",
              "Preço Unitário    0\n",
              "Quantidade        0\n",
              "Valor Desconto    0\n",
              "Valor Venda       0\n",
              "Produto           0\n",
              "Fabricante        0\n",
              "Marca             0\n",
              "Classe            0\n",
              "Cor               0\n",
              "custo             0\n",
              "lucro             0\n",
              "Tempo_envio       0\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Mh40m00N0lQE",
        "colab_type": "text"
      },
      "source": [
        "**E, se a gente quiser saber o Lucro por Ano e Por Marca?**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7CPhZjrJ00a1",
        "colab_type": "code",
        "outputId": "08a87137-f56d-4a34-891d-679beef065b8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 153
        }
      },
      "source": [
        "#Vamos Agrupar por ano e marca\n",
        "df.groupby([df[\"Data Venda\"].dt.year, \"Marca\"])[\"lucro\"].sum()"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Data Venda  Marca          \n",
              "2008        Adventure Works             306,641.16\n",
              "            Contoso                      56,416.00\n",
              "            Fabrikam                  1,557,020.55\n",
              "2009        Adventure Works             405,395.08\n",
              "            Contoso                     138,258.95\n",
              "            Fabrikam                  1,034,091.35\n",
              "Name: lucro, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kZ3lxKGabXeq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        " pd.options.display.float_format = '{:20,.2f}'.format"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "knQfX6NC3GMc",
        "colab_type": "code",
        "outputId": "8030fd21-9a09-4637-fe4f-97361465cbf4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        }
      },
      "source": [
        "#Resetando o index\n",
        "lucro_ano = df.groupby([df[\"Data Venda\"].dt.year, \"Marca\"])[\"lucro\"].sum().reset_index()\n",
        "lucro_ano"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Marca</th>\n",
              "      <th>lucro</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2008</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>306,641.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2008</td>\n",
              "      <td>Contoso</td>\n",
              "      <td>56,416.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2008</td>\n",
              "      <td>Fabrikam</td>\n",
              "      <td>1,557,020.55</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2009</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>405,395.08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2009</td>\n",
              "      <td>Contoso</td>\n",
              "      <td>138,258.95</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>2009</td>\n",
              "      <td>Fabrikam</td>\n",
              "      <td>1,034,091.35</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Data Venda            Marca                lucro\n",
              "0        2008  Adventure Works           306,641.16\n",
              "1        2008          Contoso            56,416.00\n",
              "2        2008         Fabrikam         1,557,020.55\n",
              "3        2009  Adventure Works           405,395.08\n",
              "4        2009          Contoso           138,258.95\n",
              "5        2009         Fabrikam         1,034,091.35"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0xu9qx1x4WM6",
        "colab_type": "code",
        "outputId": "28166c13-06a7-4532-908a-2cd10156422b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "#Qual o total de produtos vendidos?\n",
        "df.groupby(\"Produto\")[\"Quantidade\"].sum().sort_values(ascending=False)"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Produto\n",
              "Headphone Adapter for Contoso Phone E130 Silver    25232\n",
              "Headphone Adapter for Contoso Phone E130 White     25008\n",
              "Adventure Works Laptop15.4W M1548 Black             1089\n",
              "Fabrikam Trendsetter 2/3'' 17mm X100 Grey           1087\n",
              "Adventure Works Laptop15.4W M1548 Red               1047\n",
              "Fabrikam Trendsetter 2/3'' 17mm X100 Black           926\n",
              "Fabrikam Trendsetter 1/3'' 8.5mm X200 Black          884\n",
              "Fabrikam Trendsetter 1/3'' 8.5mm X200 Grey           845\n",
              "Fabrikam Trendsetter 1/3'' 8.5mm X200 White          789\n",
              "Name: Quantidade, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ov8qN2bI56NI",
        "colab_type": "code",
        "outputId": "f7f81f4d-dd72-4500-dd5d-3459964fbaff",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 376
        }
      },
      "source": [
        "#Gráfico Total de produtos vendidos\n",
        "df.groupby(\"Produto\")[\"Quantidade\"].sum().sort_values(ascending=True).plot.barh(title=\"Total Produtos Vendidos\")\n",
        "plt.xlabel(\"Total\")\n",
        "plt.ylabel(\"Produto\");"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAscAAAFnCAYAAABKAuRdAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAgAElEQVR4nOzde1zO5//A8VelUM5JyvnQF98ox+V8mkOMaWSibodpG5ZmmlNEkjnMtK3M5hQ6yIyhIofENpRDREbOVE7RgdDxvn9/VJ9vqSxbm/229/Px8JjP4bqu9/W+7z32vq/7uj/T0mg0GoQQQgghhBBov+4AhBBCCCGE+LuQ4lgIIYQQQoh8UhwLIYQQQgiRT4pjIYQQQggh8klxLIQQQgghRD4pjoUQQgghhMgnxbEQQojXYsGCBVhbW2NtbY25uTl9+vRRjtPT00ts8/DhQ8LDw3+zb29vb+bOnVvsfFRUFK1bt1bGGTBgAO+//z7x8fF/eD7jx49nx44dL70nKyuLnTt3/uGxAD799FOWL19e7Pwvv/xC7969UavVf3iMXbt2oVKpAJg5cyaHDh0qds+9e/do0aLFHx5LiL8LKY6FEEK8FgsXLiQsLIywsDCMjY35/PPPleMqVaqU2CYqKqrEAu1VmJiYKOPs37+fTp064eLi8of6LKtff/213Irj4cOHExoaWqwI3rVrF8OGDUNbu3z/E798+XL69u1brn0K8XckxbEQQoi/nb179zJkyBCsra0ZO3Yst2/f5sKFC3h4eLBv3z4++eQTALZt28agQYMYMGAA9vb2JCYmvvJYDg4OxMTE8OTJE3bs2IGTkxPjxo1TVmU3b97M4MGDsba2ZvLkySQnJwMQHx/PyJEj6devHy4uLuTm5gKQkJDAf//7X6X/guOHDx/i5OTE2bNnGTNmDJBX7L/zzjtYW1szcuRIzp8/D8D9+/cZN24cgwcPpl+/fnh5eRWLu3PnzmhpaREVFaWce/78OQcPHmT48OE8fvyYGTNmMHDgQN588022b9+u3NeiRQt27tyJjY0N3bt3Z+PGjQCo1Wo8PDzo3bs3tra2XLp0SWmjUqnYtWsXAD/88AN9+vRh6NCh7N69W7lHrVbj5eWlrMzPnj2bZ8+eFXlNBw0axNChQ4vELcTfiRTHQggh/lbu3LmDm5sbq1atIiwsjN69ezN//nzMzc1xcHBg4MCBeHl58ejRIzw8PPD19WX//v00bNiQb7755pXHy83NRVtbG11dXQCOHj3KwoULmTlzJmfPnmX9+vX4+fkRFhaGqakpX3zxBQArVqygS5cuHDx4kHHjxhEdHf3ScWrXrs306dNp27YtgYGBPH36lI8//ph58+YRFhaGo6Mjn376KWq1mo0bN9KpUyf27NlDcHAw8fHxPHjwoEh/2traDBs2rEhxeuDAAVq2bEmjRo1YunQp2tra7N27l23btuHt7c3ly5eVe69evcrOnTv55ptvWLlyJbm5ufz8888cPXqU0NBQ/P39OXXqVLF5pKWlsXjxYtatW0dwcHCRuPbu3ctPP/3Ejh07CA0N5fHjx0rhvXDhQr777jv27t3LggUL/vA3AEL8WaQ4FkII8bdy9OhRrKysaNSoEQAjR44kKiqKnJycIvcZGhpy+vRp6tatC0DHjh1fee9wbm4u69ato0ePHlSqVAmAxo0b07hxYwAOHz7MwIEDMTQ0VGI5evQoAKdOnWLw4MEAWFhY0LRp01ca+9y5c9StW5cOHToAMHDgQFJSUkhMTMTQ0JBffvmFU6dOoaenx8qVK6lTp06xPoYPH87+/fvJyMgA8rZUDB8+HICIiAjGjh2LtrY2tWrVon///uzfv19pO2zYMADMzc3JzMzk0aNHnDx5kl69emFgYEClSpUYNGhQsTFjYmJo1KgRzZo1A8DGxka5dvjwYWxsbNDX10dHR4fhw4cr+TI0NCQoKIjExEQ6duzInDlzXilfQvxVKrzuAIQQQojCUlJSqFatmnJctWpVNBoNKSkpRe7Lzc3l66+/5tChQ+Tm5vL06VOaNGnym/3fvXsXa2tr5djCwoKlS5cqx9WrV1f+npycXKQorVatGo8ePQLyVlAL740uHHNZJCcnF2tTtWpVHj16xPjx41Gr1SxcuJAHDx5gb2/P1KlT0dLSKnJ/o0aN+M9//sOhQ4d44403OHPmDF999RUAT548Ydq0aejo6ACQmZlZZN5Vq1YFUK6r1WrS0tKKzfdFaWlpSlsonq/Cx9WrV1fytXr1alavXs3w4cMxMTHB1dWVN9544xUyJsRfQ4pjIYQQfyuGhoacOXNGOU5LS0NbW5uaNWsWuW/Pnj0cOnQIf39/atWqxffff09wcPBv9l/wg7yyqF27NqmpqcpxamoqtWvXBvIKx8JP1SjYi6yjo4NarUaj0aClpcXjx49LnWfhvjUaDWlpaRgaGlKhQgU++OADPvjgA27cuMH7779Phw4d6NatW7F+hg8fTkhICI8ePaJv375KwV6nTh1WrVrFf/7znzLNtWBOT548KTanst7zsnw1bNiQJUuWoFar2blzJy4uLvz8889ljk2Iv4psqxBCCPG30q1bN06dOqVskQgKCqJbt25UqFCBChUqKIXZo0ePqFevHrVq1SIlJYW9e/fy9OnTco2ld+/eHDhwQFm1DgoKolevXgC0bduWAwcOABAdHc3t27cBqFmzJjo6OsTFxQEUeTpFhQoVSE9PR6PRYGFhwcOHD5UPAqGhodStW5f69eszf/58ZTtCw4YNqV27drFV4wKDBg0iOjqakJAQZUsFQN++fQkKCgIgJyeHzz77jAsXLrx0vu3ateOXX37h+fPnPH/+vMQPEW3atOHGjRvcvHkTgB9//LFIvnbv3s3z58/Jycnhhx9+oFevXiQnJzNhwgTS09PR1tbG0tKy1PkI8brJyrEQQoi/lbp16+Lp6cmUKVPIzs6mfv36LFq0CMgrnH19fRkxYgTfffcdoaGh9O/fnwYNGjBt2jQmT57M0qVLMTAwKJdYLCws+OCDD7C3t0etVtOqVSvc3d0BmDFjBi4uLuzatQtLS0u6du0KQKVKlZg6dSqOjo7UqVNHeU4wQIcOHVixYgU9evTgyJEjfPnllyxatIhnz55Rq1YtVq5ciZaWFnZ2dsyfP59Fixah0Wjo27cvXbp0KTHGKlWq0L17d06dOkXnzp2V89OmTWPhwoUMHDgQgB49evzm84j79OnD4cOHsba2pnbt2vTq1avYj/Jq1arFrFmzmDBhAgYGBowcOVK5Zm1tTVxcHMOHD0ej0WBlZcXYsWOpWLEiPXr0YMSIEejo6KCrq8vixYvL/kII8RfS0mg0mtcdhBBCCCGEEH8Hsq1CCCGEEEKIfFIcCyGEEEIIkU+KYyGEEEIIIfJJcSyEEEIIIUQ+KY6FEEIIIYTIJ49yE0KQk5NLSsqz1x3GP0bNmvqSz3Ik+Sx/ktPyJfksX39FPo2MqpZ6TVaOhRBUqKDzukP4R5F8li/JZ/mTnJYvyWf5et35lOJYCCGEEEKIfFIcCyGEEEIIkU+KYyGEEEIIIfJJcSyEEEIIIUQ+KY6FEEIIIYTIJ8WxEEIIIYQQ+eQ5x0IIhrrset0hCCGEECXaMLvvXzqerBwLIYQQQgiRT4pjIYQQQggh8klxLIQQQgghRD4pjoUQQgghhMj3pxXHCQkJDB8+vMg5b29v/P39/1C/zs7OREVFlXq9b9++PH369A+NURbfffcdnTt3Jicnp8Try5YtY8eOHa/c7759+35XPMHBwQwcOJBTp069cttz586hUqkYNWoUw4cPx8fHB41G88r9hIWFvXKb37Jjxw569eqFSqXCwcEBlUrF1atXAVCpVFy+fLncxyxs9uzZDB06FJVKpfzx9fUFIC0tjYkTJ+Ls7Kzc/+jRIxwdHVGpVNjZ2RETEwPApUuXsLOzw87OjgULFpQ41pdffsm7776rtL148SIAn3zyCRkZGcyePZuIiIg/db5CCCHEv52sHP9OISEh1KhRg2PHjpVbnwkJCYSGhv6utseOHWPGjBl07Njxldqlp6czY8YM3Nzc2Lp1K1u3buXixYts27btlfrJyspi48aNr9SmrAYPHoyfnx/+/v5MnToVT0/PP2Wc0kyfPh0/Pz/lz4QJEwBYsGABHTp0KHLv7t27GTZsGH5+fkyfPp2vvvoKgMWLF+Pq6kpQUBDp6ekcOXKkSLsTJ05w8eJFtm7dip+fH9OmTWPdunUAeHl5UalSpb9gpkIIIYR4bY9yCwgIIDg4GG1tbfr168d7773HvXv3mDFjBgA5OTksW7aMhg0bsnbtWkJDQzE1NSU9PR3IW4W+d+8ed+/eJSkpiRkzZtCzZ0+l7yNHjpCbm8u6deuoWLEi8+fPJz4+nqysLJydnenevTv9+/dn1KhRREREkJWVha+vL5UrV8bNzY34+HhycnJwdnamS5cuRWKPi4tDrVbz3nvvERoaqoy7a9cu1q1bh7GxMZUqVcLMzIz09HRcXFx49uwZGRkZuLm5YWFhQd++fbGxsSEyMhJdXV28vb3x8PDg3Llz+Pj4MH78eFxdXUlLSyM3N5d58+bRsmVLBgwYQM+ePTE0NGTy5MkAHD16lJ9++onY2FiqVavGw4cP2bhxIzo6OpibmzNv3jy8vb2Jj48nISEBPz8/dHR0gLwV5zfffJP//Oc/AOjq6rJs2TIqV64MwPLly4mOjiY3Nxd7e3tsbGxQqVR07dqVyMhIUlJS+Pbbb1m7di1xcXG4u7szd+7cEvO9Zs0aDhw4gLa2Nn369GHSpElERUXh5eVFhQoVMDY2ZsmSJejp6ZX6vrG0tOTWrVvK8d69e1m8eDGpqamsXr0aU1PTMsdsamqKl5cXp06dIjc3FwcHB4YMGVLm97CnpycXLlzg0qVLyrmCwhng7t27GBsbk5WVRWJiIhYWFgD06dOH48eP06tXL+Xex48f8+zZM3Jzc6lQoQKdO3emc+fOQN63IcHBwcq977zzDqtWrcLU1JTExESmTp3Ktm3bSnzfqlQqzMzMAJg/f36Z5yaEEEL8W/2pxfGNGzdQqVTKcWJiIu+99x7x8fGEhYWxZcsWAEaPHo21tTUPHz7ko48+onPnzvzwww8EBgYyZcoUtmzZwt69e8nOzqZ///5Kf/fv32fDhg3ExcUxa9YspUg1MzPjgw8+YPr06URGRpKeno6enh7+/v7cv3+fsWPHsm/fPnJzc2natCmOjo588sknyr1GRkZ89tlnJCcnM27cuCKFCeStGg8ePJgBAwawcuVKMjMz0dPTw8vLi+3bt1OtWjVlS0lSUhIjR46kX79+HD9+nLVr1+Lt7Q1As2bNcHZ2ZunSpfz4449MnDiRgIAAnJycWLVqFT169GDkyJFcvXqVxYsX4+vrS05ODj179lTmCtCtWzd69OjBwIEDMTc3x8bGhp07d2JgYMCkSZOIjIwEIDs7m8DAwCJzuX79ulK0FahSpQoAJ0+e5MqVKwQFBfHs2TPefvtt+vXrp9yzadMmVqxYwf79+5k4cSIxMTG4u7uzc+fOEvO9YcMGfvnlF3R0dJTXfsGCBfj6+mJiYoKHhwfBwcGMGDGi1PdUREQEbdq0UY4NDQ3ZtGkTX3zxBfv378fc3LzMMbdu3ZrExEQCAgLIysrinXfeoV+/fmVepS3I04uSkpKYNGkST58+ZdOmTaSkpFCtWrUiMSclJRVp07NnTwICAujXrx89e/bkzTffpGfPnmhpaRXrv1+/fkRERGBvb094eDgDBgwgODi41PetmZkZo0ePLtOchBBCiL8bI6Oqf+l4f2px3KRJE/z8/JTjgqLw/Pnz3Lp1i7FjxwLw9OlTEhMTqV+/Pp6ennh7e/P48WPMzc25desWzZs3p2LFilSsWBFzc3Olv4IV3RYtWnD//n3lfMFX3cbGxjx58oQLFy5gZWWlnNPT0yM1NRVA2YZQt25dnjx5wtmzZzl9+jTR0dEAZGZmkpWVpaxmajQaQkND8fX1pUaNGrRt25YjR47QsWNHDAwMMDQ0BKB9+/YA1K5dm2+++Yb169eTlZWFvr5+sfjbtm1LZGQkLVu2VK6dOXOG5ORkdu/eDcDz58+Vay8Ws4XdvHmTRo0aYWBgAMAbb7yh7F0tqZ2Wlha5ubkl9hUbG0unTp0A0NfXp3nz5sqqbeG8FeSycLuS8j1w4EAmTJjAkCFDePvtt0lNTUVLSwsTExMArKysOHnyZLE49uzZQ2xsLBqNBiMjI+bOnatcK/xap6amvlLM0dHRxMTEKB/g1Go1SUlJNGjQoMj4K1euZMOGDcrx9OnTadeuXYk5AzAyMmL79u0cOXKEOXPmsGTJkiLXS9rPraenh6+vL+fPn+fYsWMsWbKEPXv2sGzZsmL3DhgwgKVLlyrFsbu7Oxs3bizxfQsvf78IIYQQf3dJSU/Kvc+XFdyvZVuFrq4uvXv3xsPDo8j5OXPm0L17d0aPHk1YWBiHDx9Go9Ggrf2/rdGFCwu1Wl1i/wVbBgrfX7hdVlaW0ueL9+rq6jJp0qRSv16Pjo7m0aNHyo+wnjx5QmhoKB07diwxzk2bNmFsbMznn3/O+fPnWb58eYmxvbhCqKuri5ubW4lFmK6ubomxQV6xW3iu2dnZVKxYsdR2TZs25fz589jY2CjnkpOTef78ebGYsrOzS83bi0rK98KFC7l27Rp79+5FpVKxfv36YrGWtFI6ePBgZs2aVeJ8X4zjVWLW09PD1taWDz/8sMS+C0yfPp0+ffq89J4CJ06coEWLFlSvXp1evXoxc+ZMatWqVeQDxP3796lTp06Rdrm5uajVatq0aUObNm1QqVT07NmzxA8uZmZmPHjwgLt37/LkyROaNGny0vfty94vQgghhCjqtfwgz9zcnKioKJ4/f45Go8HT05OMjAxSUlJo2LAhGo2G8PBwsrOzadiwIdeuXSMrK4v09HRiY2OVfk6fPg3kPQnA1NS01PHatGmjPOHi7t27aGtrF/mauzBLS0vCw8OBvCcPrFy5ssj1kJAQPv30U3bt2sWuXbsICQnh5MmT6Onp8eTJEx4/fkx2drayglcwJ4CDBw+SnZ2t9FXwZImzZ8/SvHlztLW1ladfWFpacvDgQQCuXr2qPCHhtzRu3Jhbt24pe7NPnDhB69atS71/6NChHD58mHPnzgF5hay7uzvHjh2jdevWSt6ePn3K7du3adSoUYn9aGtrK4VcSfnW0tLCx8eHZs2a4eTkRPXq1ZXzd+7cKVOsZfEqMVtYWBAREYFarSYzM5NFixb9obEB9u/fz48//gjk7U03MTFBV1eXpk2bKq/3/v376dGjR5F2X3/9NT4+PspxcnIytWvXLlLQF9a7d2+8vLzo2zfvf6n5W+9bIYQQQpTNa1k5NjU1ZezYsdjb26Ojo6Ps8xw1ahSLFi2iXr16qFQq3NzciI2NxcbGBjs7O+rXr19kv2mVKlWYNGkSiYmJuLq6ljreW2+9xYkTJ1CpVGRnZxdbsS5s0KBBREZGYmdnR25uLk5OTsq1nJwcDh06VOTRXfr6+vTu3ZtDhw7h5OSEg4MD9erVU34ENWzYMGbNmkVYWBj29vaEhISwfft2AC5cuEBgYCBaWlpMnTqVrKwsfv31Vz777DOcnZ2ZM2cOY8aMQa1WF9lK8DL6+vrMnDkTR0dHtLW16dChAx07duT48eMl3m9gYMDatWtZsGABGRkZ6OjoMHToUEaOHAnkFZv29vbk5OTg4uJSZFtIYUZGRmRnZ+Ps7MzKlSuL5btq1aqkpKRga2uLvr4+7dq1o0aNGixatAgXFxcqVKhAgwYNeOutt8o0z9J07NixzDG3b98eKysrRo0ahUajYcyYMSXe9+K2imbNmuHm5sb48eN5/Pgx9+/fR6VSMWXKFKZMmcLs2bM5cOCA8kEDwNXVlfnz56NWq7G0tKRr165Fxpg0aRIeHh68++67VK5cGbVaXeKWigL9+/fHzs5O2XbzsvetEEIIIcpOS/N7Hmj7N+Dt7U3NmjVxcHB43aH8LgVPICjYGyzE6zTUZdfrDkEIIYQo0YbZfcu9z5ftOZbnHAshhBBCCJHvtT3n+I+aOnXq6w7hDzl06NDrDkEIIYQQQrxAVo6FEEIIIYTI9/92z7EQonz9Gc+R/LcyMqoq+SxHks/yJzktX5LP8vVX5FP2HAshhBBCCFEGUhwLIYQQQgiRT4pjIYQQQggh8klxLIQQQgghRD4pjoUQQgghhMgnxbEQQgghhBD5pDgWQgghhBAinxTHQgghhBBC5JPiWAghhBBCiHxSHAshhBBCCJFPimMhhBBCCCHySXEshBBCCCFEPimOhRBCCCGEyCfFsRBCCCGEEPmkOBZCCCGEECJfhdcdgBDi9Rvqsut1hyCEEEIAEPzFsNc6vqwcCyGEEEIIkU+KYyGEEEIIIfJJcSyEEEIIIUQ+KY6FEEIIIYTI96cUxwkJCQwfPrzIOW9vb/z9/f9Qv87OzkRFRZV6vW/fvjx9+vQPjVEW3333HZ07dyYnJ6fE68uWLWPHjh2v3O++fft+VzzBwcEMHDiQU6dOvXLbc+fOoVKpGDVqFMOHD8fHxweNRvPK/YSFhb1ym9+yY8cOevXqhUqlwsHBAZVKxdWrVwFQqVRcvny53McsbPbs2QwdOhSVSqX88fX1BSAtLY2JEyfi7Oys3P/o0SMcHR1RqVTY2dkRExMDwKVLl7Czs8POzo4FCxYUGSM3N5cuXbqQkZGhHLdv316ZJ4CNjQ3Xr18v8f39008/ERgYCPw5r4EQQgjxbyMrx79DSEgINWrU4NixY+XWZ0JCAqGhob+r7bFjx5gxYwYdO3Z8pXbp6enMmDEDNzc3tm7dytatW7l48SLbtm17pX6ysrLYuHHjK7Upq8GDB+Pn54e/vz9Tp07F09PzTxmnNNOnT8fPz0/5M2HCBAAWLFhAhw4dity7e/duhg0bhp+fH9OnT+err74CYPHixbi6uhIUFER6ejpHjhxR2ujo6GBpacnZs2cBuHjxItWqVePkyZMAPHnyhJSUFJo2bVpifD179mTMmDEArFmzpnwnL4QQQvwLvZZHuQUEBBAcHIy2tjb9+vXjvffe4969e8yYMQOAnJwcli1bRsOGDVm7di2hoaGYmpqSnp4O5K1C37t3j7t375KUlMSMGTPo2bOn0veRI0fIzc1l3bp1VKxYkfnz5xMfH09WVhbOzs50796d/v37M2rUKCIiIsjKysLX15fKlSvj5uZGfHw8OTk5ODs706VLlyKxx8XFoVaree+99wgNDVXG3bVrF+vWrcPY2JhKlSphZmZGeno6Li4uPHv2jIyMDNzc3LCwsKBv377Y2NgQGRmJrq4u3t7eeHh4cO7cOXx8fBg/fjyurq6kpaWRm5vLvHnzaNmyJQMGDKBnz54YGhoyefJkAI4ePcpPP/1EbGws1apV4+HDh2zcuBEdHR3Mzc2ZN28e3t7exMfHk5CQgJ+fHzo6OkDeivObb77Jf/7zHwB0dXVZtmwZlStXBmD58uVER0eTm5uLvb09NjY2qFQqunbtSmRkJCkpKXz77besXbuWuLg43N3dmTt3bon5XrNmDQcOHEBbW5s+ffowadIkoqKi8PLyokKFChgbG7NkyRL09PRKfd9YWlpy69Yt5Xjv3r0sXryY1NRUVq9ejampaZljNjU1xcvLi1OnTpGbm4uDgwNDhgwp83vY09OTCxcucOnSJeVcQeEMcPfuXYyNjcnKyiIxMRELCwsA+vTpw/Hjx+nVq5dyb+fOnTl16pTyT1tbW06dOsXo0aOJjo4u8qHnxff3/v37uXLlCoaGhsTFxeHk5ISPj88fmpsQQgjxb/anrRzfuHGjyNfRP/74IwDx8fGEhYWxZcsWAgIC2L9/P3fu3OHBgwd89NFH+Pn5MWLECAIDA3n8+DFbtmxh69atLF++nCtXrij9379/nw0bNrBixQpWrlypnDczMyMgIABTU1MiIyMJDQ1FT08Pf39/vL29WbRoEZD39XXTpk0JCAigfv36REZGEhwcjJGREX5+fqxatYrPPvus2LxCQkIYPHgwAwYM4MiRI2RmZqLRaPDy8mLjxo2sXr1aKeCSkpIYOXKkspK4du1apZ9mzZoRGBhIq1at+PHHH5k4cSJvvPEGTk5ObNq0iR49erBp0ybc3d1ZtmwZkPehoWfPnkphDNCtWzd69OjB9OnTMTc3x8vLC19fX7Zs2UJCQgKRkZEAZGdnExgYqBTGANevX6dVq1ZF5lelShV0dHQ4efIkV65cISgoiE2bNuHj46N8OKlSpQqbNm2iZ8+e7N+/n4kTJ9KkSRPc3d1LzfeGDRvYsmULQUFBVKtWDchbffXy8sLf35/q1asTHBz80vdUREQEbdq0UY4NDQ2LxPEqMZ86dYrExEQCAgLYvHkzq1evVrY2lEWVKlVKPJ+UlMSIESNYvXo106ZNIyUlRZlvQcxJSUlF2lhZWSkrxadPn2bYsGHcuHEDQCmaC7z4/i7g6OhIlSpV8PHx+cNzE0IIIf7N/rSV4yZNmuDn56cce3t7A3D+/Hlu3brF2LFjAXj69CmJiYnUr18fT09PvL29efz4Mebm5ty6dYvmzZtTsWJFKlasiLm5udJfwYpuixYtuH//vnK+4KtuY2Njnjx5woULF7CyslLO6enpkZqaCqCsyNWtW5cnT55w9uxZTp8+TXR0NACZmZlkZWUpq5kajYbQ0FB8fX2pUaMGbdu25ciRI3Ts2BEDAwMMDQ0BaN++PQC1a9fmm2++Yf369WRlZaGvr18s/rZt2xIZGUnLli2Va2fOnCE5OZndu3cD8Pz5c+VawQpkSW7evEmjRo0wMDAA4I033uDixYulttPS0iI3N7fEvmJjY+nUqRMA+vr6NG/eXCn6C+etIJeF25WU74EDBzJhwgSGDBnC22+/TWpqKlpaWpiYmABFC8TC9uzZQ2xsLBqNBiMjI+bOnatcK/xap6amvlLM0dHRxMTEoFKpAFCr1SQlJdGgQYMi469cuZINGzYox9OnT6ddu3Yl5gzAyMiI7du3c+TIEebMmcOSJUuKXC9pP3eLFi24efOmssrcoEEDTE1NicPyR7kAACAASURBVI+P59SpU4wcObLEOT958qTEGMo6NyGEEOLvysio6msb+y/fVqGrq0vv3r3x8PAocn7OnDl0796d0aNHExYWxuHDh9FoNGhr/29xu3BhoVarS+y/8Mpowf2F22VlZSl9vnivrq4ukyZNKvUr6OjoaB49eqT8COvJkyeEhobSsWPHEuPctGkTxsbGfP7555w/f57ly5eXGJuWllaxHLm5uZVYhOnq6pYYG+QVu4Xnmp2dTcWKFUtt17RpU86fP4+NjY1yLjk5mefPnxeLKTs7u9S8vaikfC9cuJBr166xd+9eVCoV69evLxbri2NC3p7jWbNmlTjfF+N4lZj19PSwtbXlww8/LLHvAtOnT6dPnz4vvafAiRMnaNGiBdWrV6dXr17MnDmTWrVqFfkAcf/+ferUqVOknba2Nm3atGHPnj00btwYyCuCIyMjefToEQ0bNix1ziUp69yEEEKIv6ukpJIXgMrLy4rvv/wHeebm5kRFRfH8+XM0Gg2enp5kZGSQkpJCw4YN0Wg0hIeHk52dTcOGDbl27RpZWVmkp6cTGxur9HP69Gkg70kApqampY7Xpk0b5QkXd+/eRVtbu8jX3IVZWloSHh4O5D15oPB2DcjbUvHpp5+ya9cudu3aRUhICCdPnkRPT48nT57w+PFjsrOzlZXngjkBHDx4kOzsbKWvgidLnD17lubNm6Otra08/cLS0pKDBw8CcPXqVeUJCb+lcePG3Lp1S9lKcOLECVq3bl3q/UOHDuXw4cOcO3cOyCtk3d3dOXbsGK1bt1by9vTpU27fvk2jRo1K7EdbW1tZgS4p31paWvj4+NCsWTOcnJyoXr26cv7OnTtlirUsXiVmCwsLIiIiUKvVZGZmKts//oj9+/cr24fi4uIwMTFBV1eXpk2bKq/3/v376dGjR7G2VlZWBAQEKCvDHTp04IcffnjpKvWLCorlP2NuQgghxL/FX75ybGpqytixY7G3t0dHR4d+/fpRqVIlRo0axaJFi6hXrx4qlQo3NzdiY2OxsbHBzs6O+vXrF9lvWqVKFSZNmkRiYiKurq6ljvfWW29x4sQJVCoV2dnZxVasCxs0aBCRkZHY2dmRm5uLk5OTci0nJ4dDhw4VeXSXvr4+vXv35tChQzg5OeHg4EC9evUwMzMDYNiwYcyaNYuwsDDs7e0JCQlh+/btAFy4cIHAwEC0tLSYOnUqWVlZ/Prrr3z22Wc4OzszZ84cxowZg1qtLrKV4GX09fWZOXMmjo6OaGtr06FDBzp27Mjx48dLvN/AwIC1a9eyYMECMjIy0NHRYejQocrX+K1bt8be3p6cnBxcXFyKbAspzMjIiOzsbJydnVm5cmWxfFetWpWUlBRsbW3R19enXbt21KhRg0WLFuHi4kKFChVo0KABb731VpnmWZqOHTuWOeb27dtjZWXFqFGj0Gg0yhMfXvTitopmzZrh5ubG+PHjefz4Mffv30elUjFlyhSmTJnC7NmzOXDggPJBA8DV1ZX58+ejVquxtLSka9euxcaxsrLC09NTKWT/+9//EhcXx6hRo8o8/1atWmFra8sPP/xQprkJIYQQojgtze95qO1r5u3tTc2aNXFwcHjdofwuffv2JTg4WNkbLMTrNtRl1+sOQQghhAAg+Ith/65tFUIIIYQQQvxdvZbnHP9RU6dOfd0h/CGHDh163SEIIYQQQogSyMqxEEIIIYQQ+f5f7jkWQpS/P3t/17+JkVFVyWc5knyWP8lp+ZJ8lq+/Ip+y51gIIYQQQogykOJYCCGEEEKIfFIcCyGEEEIIkU+KYyGEEEIIIfJJcSyEEEIIIUQ+KY6FEEIIIYTIJ8WxEEIIIYQQ+aQ4FkIIIYQQIp8Ux0IIIYQQQuST4lgIIYQQQoh8UhwLIYQQQgiRT4pjIYQQQggh8klxLIQQQgghRD4pjoUQQgghhMgnxbEQQgghhBD5pDgWQgghhBAiX4XXHYAQ4vUb6rKrXPrZMLtvufQjhBBCvC6yciyEEEIIIUQ+KY6FEEIIIYTIJ8WxEEIIIYQQ+f6RxXFISAjm5uYkJyeXeN3f3x9vb+9yGSssLKxc+gFYtGgR27ZtU47d3d1Zvny5crxp0ya++OKLMvVlZWX1yuP/njaF3blzh3Pnzv2utps3b8bc3JynT58q58zNzVGpVMqf3NzcEtv+/PPPtGjRAvh9OZw9ezYTJ04sci4iIoIWLVqQkJAAwOXLl+nXrx/+/v5F2g0dOlSJ7/Dhw0X6mD59OrNnzwbg/v37TJw4EZVKhb29PbGxscXmUXi+tra2HDhwAABvb+8i45aFSqXi8uXLr9RGCCGEEP/QH+SFhITQoEED9u3bx+jRo//UsdasWYO1tXW59GVlZUV4eDgjR44E4Nq1a2hr/+/zy+nTp3n33XfLZaw/Q2RkJM+ePcPCwuKV2u3cuZNHjx5Rp06dIuerVKmCn5/fS9tmZmayZs0ajIyMgN+fw4SEBJKTk6lVqxYAe/bsoUGDBgA8e/aMRYsW0aVLl2Ltpk+fTp8+fYqdP3r0KLdv36Z58+YAbNy4kf79+2NnZ0d0dDReXl6sX7++1PneuXOHCRMm0L9//5fOXwghhBDl6x+3cpyamsq5c+eYPXs2oaGhyvnjx48zdOhQJkyYoKxufvTRR5w8eRKAjIwM+vbtS25uLl5eXtjb22NnZ0dISAiQt0q4cuVKJk6cyKBBg7hw4QLr1q0jLi4OJycnoqKicHZ2VsYrWIVVqVR4eHjg4eFBeno6zs7OjBs3DgcHBy5dulQk9k6dOnH69GllHnp6eqjVap4/fw5ATEwM7du3Jy4uDnt7e1QqFZMmTSI1NZWoqCg+/PBDVCpVkVXJixcvYmdnx9OnT/H09MTOzo6RI0eyY8eOMuXz0qVLjB49GpVKxbhx40hNTSUhIYERI0bg4uLCiBEjcHd3Jzk5GR8fHzZv3kx4eHipMTo6OjJlyhRsbGxYvXo1AP369eOTTz5BS0ur7C90vm+//ZYxY8agp6f3Sjl8Uffu3dm7dy+Q9164efMmJiYmAOjp6bF27dpixXtpsrKyWL16NZMnT1bO1axZk9TUVAAeP35MzZo1X9rHw4cPMTY2LnIuJycHFxcXHBwcGD58OBEREQD8+uuvjBo1Cjs7O5YtW1akTXp6OiNHjuTKlStlil0IIYT4t/vHFcdhYWH07t2bHj16cPPmTe7fvw/AF198weeff46vry8pKSkA9O/fn0OHDgF5K33dunXjzJkzJCYmEhAQwObNm1m9ejUZGRlAXtGzfv16xo4dy86dO3F0dKRKlSr4+Pi8NCYzMzPmz5/Ppk2b6NGjB5s2bcLd3b1YIVOzZk0MDAy4d+8e0dHRtG3bljZt2nDmzBmuX7+Oqakp+vr6LF68mJkzZ+Ln50enTp3YvHkzkPfV//r162ndujUAycnJLFiwgJUrV5Kdnc3hw4cJCgoiMDCQnJycMuXz0aNHuLm54efnR/v27QkODgYgLi6OTz/9lB9++IHz58/z4MED3nnnHcaOHcubb75ZaoyxsbF8/vnnbN26lW3btpGSkkKVKlVKHDsrKwsXFxfs7Ozw9fUtdv3GjRtcunSJQYMGvXIOXzRgwADlw9Thw4fp2rWrcq1ChQpUqlSpxBj9/f0ZO3Ysn3zyibKN57vvvmP06NFF5jV+/Hj27NmDtbU18+bN4+OPPy7WV3p6OiqVCjs7OyZNmsRHH31U5HpaWhrdu3fH39+fr776Stka5OnpycKFCwkKCuLRo0ckJiYCoNFomDVrFk5OTpiZmZUYvxBCCCGK+sdtqwgJCWHKlCno6OhgbW3Nnj17mDBhAomJibRs2RLIW13MzMykb9++rF+/nlmzZhEeHs7gwYOJjo4mJiYGlUoFgFqtJikpCYCOHTsCULdu3VfaW1uwzeDMmTMkJyeze/duAGU1szArKytOnDjBpUuX6NGjB8+ePePUqVOYmJgoq9HXrl3D0tJSud/HxwcrKytatGihrKBqNBo++eQTHB0dMTU1BaBx48ZMnjwZa2trbGxsyhS7oaEhK1asICMjgwcPHjB06FClr4KVVUtLS65fv16kXWkxWlpaYmBgAOR9aIiPjy91FXXmzJm8/fbbaGlp4eDgQMeOHWnTpo1yfcmSJcybN+935fBF9erVIzs7mzt37rBnzx4mT55MdHT0S3MzbNgwatSoQatWrVizZg0+Pj6MHTuW2NhYpk6dSlRUlHLvunXrGDRoEJMnTyYiIoJly5YV+1BVeFtFUlIS48ePJyAgQLlerVo1zp8/z9atW9HW1lZWom/cuKG8twvvr161ahUmJib06tXrpfMoT0ZGVf+ysf7uJBflS/JZ/iSn5UvyWb5eZz7/UcXxvXv3iImJYenSpWhpaZGRkUHVqlWZMGFCkX2nGo0GyCs26tSpw/Xr1zlz5gweHh5cvXoVW1tbPvzww2L96+joFOujwItbAgqvzOrq6ir/dHNzo127dqXOwcrKip9//pnLly/j5OREZmYmgYGBJCYmlljQZmdnK3MrKIwhbxWyRYsWBAUFMWDAACCvQLtw4QIhISHs2rWLDRs2lBpHgcWLF/P+++/Ts2dP1q9fz7Nnz4C8Dw2Fc/GyLRGFY3yx3csU3i/euXNnLl++rBTH9+/f5/r163z66acAPHjwAAcHB/z9/V85hwUGDhzIjz/+yI0bN2jVqtVLYwOK7EHu27cv7u7uHD58mDt37vDuu++Snp5OcnIya9euJTo6mmnTpgHQrVs3Fi5c+NK+jYyMaN68eZGtNyEhIaSlpREYGEhqaiq2trYARd7bhVWrVo2jR4+SkpLym9s4yktS0pO/ZJy/OyOjqpKLciT5LH+S0/Il+Sxff0U+X1Z8/6O2VYSEhGBvb8/u3bvZtWsXYWFhpKWlcfv2bYyNjbl+/ToajYYTJ04obfr378+3335L27ZtqVChAhYWFkRERKBWq8nMzGTRokUvHbOgwKtSpQoPHjwA8vbpFn7qQgFLS0sOHjwIwNWrV0vcKtCpUyfOnj2LtrY2+vr61KxZk6dPnxIXF6fslTUzM+PMmTMAnDx5UtlGUVjVqlVxdXXFyMiI77//noSEBOWJELNmzVJWHX9LamoqDRs2JCsriyNHjpCdnQ3A7du3efDgAWq1mpiYGJo3b46WlpbyoaC0GH/99VeeP39OZmYmV69epXHjxiWOe/36dVxcXNBoNOTk5BAdHV1ka4CxsTEHDx7k+++/5/vvv6dOnTrKEx3KksOSDBw4kM2bN9OzZ88y5Wbq1KnEx8cDEBUVhZmZGePHjyc4OJjvv/+eBQsW0Lt3b95//30aNWpETEwMAOfOnaNRo0Yv7TsrK4vLly8XuS8lJYX69eujra3NgQMHyMrKAqBZs2ZK366urly7dg2AsWPH4ujoiKenZ5nmI4QQQoh/2MpxaGhokX28Wlpa2NjYEBoayrRp0/j4448xNTWlbt26yj39+vXD09OTVatWAdC+fXusrKwYNWoUGo2GMWPGvHTMVq1aYWtry/fff4++vj52dna0a9eOevXqFbvXwcGBOXPmMGbMGNRqNXPnzi12T7Vq1dDW1sbc3Fw5Z2Zmxs2bN6lYsSIA8+bNY+HChWhpaVG9enWWLFnChQsXSozP1dWVUaNGKfup9+zZg66uLiNGjCh2b8Ge1wLjx4/HwcGBjz76iAYNGig/Lhw8eDBNmjTBy8uLq1ev0r59e8zMzHjw4AGzZs2iVq1apcbYrFkzXF1duXnzJnZ2dlSrVo3Vq1dz7NgxkpKSeP/992nbti0zZ86kbt262Nraoq2tTd++fbGwsODixYscOHCgyI8ff08OS9KgQQPq16/PwIEDi5yPjY1l2bJlJCYmUqFCBfbt24e3tzf29vZMmzaNypUro6+vz5IlS0rt+8MPP2Tu3LnKo/9Keu0L5//58+eMHz9e2boCefuiJ0+ezNmzZxkxYgR169bFx8eHuXPn4u7uDkDbtm1p1qyZ0mbEiBHs3buX8PBw3nzzzVLjE0IIIUQeLc1vfbctxAsSEhJwdnYu8xMvCkRFRREQEMDXX3/9J0Umfq+hLrvKpZ8Ns/uWSz//38lXrOVL8ln+JKflS/JZvmRbhRBCCCGEEH8T/6htFeKvUb9+/VdeNYa8Hxv+0f8LnxBCCCHEn0lWjoUQQgghhMgnK8dCCIK/GCb75YQQQghk5VgIIYQQQgiFFMdCCCGEEELkk+JYCCGEEEKIfFIcCyGEEEIIkU+KYyGEEEIIIfJJcSyEEEIIIUQ+KY6FEEIIIYTIJ8WxEEIIIYQQ+aQ4FkIIIYQQIp8Ux0IIIYQQQuST4lgIIYQQQoh8UhwLIYQQQgiRT4pjIYQQQggh8klxLIQQQgghRD4pjoUQQgghhMgnxbEQQgghhBD5KrzuAIQQr99Ql13l0s+G2X3LpR8hhBDidZGVYyGEEEIIIfJJcSyEEEIIIUQ+KY6FEEIIIYTI948ujhMSEmjXrh0qlUr5s3jx4lLvV6lUXL58+aV9Tp48ucz3vqqlS5eiUqmwtramV69eqFQqnJycyq1/KyurV24TFhZW4t9fxd27dxk/fjwODg6MHz+epKQk5dro0aN5/vw5H3/8MQ4ODowcOZKIiAggL8cJCQnMnj27WJ8nTpygS5cuyr25ublFXueBAwfy7bff/q54S5OcnMyAAQNITk4GQK1WY2try7lz50qMCeDSpUvY2dlhZ2fHggULlPPr1q3D1taWkSNHcuTIkRLH8/X1Zfjw4YwZM4YRI0awe/fucp2PEEIIIYr7x/8gr0mTJvj5+ZVbf6tXry63vl5UUATu2LGDK1euMGvWrD9trLJas2YN1tbWZGVlsXHjRqytrV+5jy+//JJ3332XwYMHExAQgK+vLzNnzuTu3bvUrVuXiIgIWrduzfvvv09iYiLvvfceffr0KbW/27dv4+vrS/v27ZVzOjo6RV5nR0dHhg0b9sqxvkytWrX44IMP+Pzzz1myZAlbt27FwsICCwuLEmMCWLx4Ma6urlhYWODi4sKRI0do2rQpe/bsISgoiPT0dMaMGUP37t3R0dFR2gUHB3Pq1CmCgoLQ09MjKSkJe3t7zM3NadasWbnOSwghhBD/848vjkuSk5PDrFmzuH//Ps+ePWPq1KlKMfbDDz9w8eJFnj9/zldffUVCQgIbNmzg2bNnzJo1i4kTJxIVFaX0lZ6ezoQJE/jss89ISkriq6++QldXl2rVqvHll19y5swZNm/ejI6ODr/++iuTJk3i559/5uLFi8ycOZN+/fr9ZryzZ89GV1eX1NRUvvzyS9zc3IiPjycnJwdnZ2e6dOmCSqWia9euREZGkpKSwrfffkudOnVwcXHh3r17tGnTRulv586d+Pv7o6urS8uWLVmwYAFXr17Fw8MDLS0tDAwMWLp0Kd9//z1xcXE4OTlhZGREXFwc7u7uuLm5lRqDmZkZAPPnz1fGW7BgARUrVgSgZs2aXLhwAYCoqCg6derE4MGDlXvv3r2LsbExAMuWLcPIyIjp06cXyYeRkRE+Pj7MnTu3xHwdO3aMxo0bY2Jiwo4dOzh58iQpKSlcuXKFTz75hJCQEK5du8aKFSswNDRk5syZNGzYkDNnzjB69Gji4uKIiYnB3t4ee3v7In2PGDGCXbt2ER4eTmBgIIGBgaXGlJWVRWJiIhYWFgD06dOH48ePk5SURI8ePdDT06NWrVrUq1ePq1ev0qJFC6Wtn58fy5cvR09PT+k/NDQUXV1dEhISmDFjBvr6+jg4OFC1alVWrlxJhQoVMDExYdGiRcycOZNRo0bRpUsXsrKyGDx4MGFhYVSo8K/8V14IIYQos3/lfynT0tLo3r0777zzDvHx8Xz88cdKcVy7dm38/Pzw9/fHz8+PPn36cPnyZfbt26cUKgU0Gg2zZs3CyckJMzMzrl69yooVK2jQoAEzZ87kl19+wcDAgIsXLxIWFsbJkyf59NNPCQ8PJyYmBj8/vzIVxwDVq1dn0aJF7Ny5EyMjIz777DOSk5MZN24cwcHBAFSpUoVNmzaxYsUK9u/fT5MmTcjJyWHr1q3KeADr169nzZo1mJiYsH37djIyMli0aBEeHh40btyYgIAAAgICmDx5MmvXrsXHx4eEhARiYmJwd3d/aQxmZmaMHj26SOz6+vpA3taHwMBAPvroIyCvOHZ0dFTus7Oz4969e8p2CFNTUwDq1KlTpL/KlSu/NFebN2/G1dVVOb558yaBgYFs27aN7777jp07d7Jjxw5CQkIYN24cFy9eZNWqVaSlpTFkyBDCw8PJzMxk6tSpxYpjLS0tFi5cyNtvv42npydVq1YtNaaUlBSqVaumHBsaGpKUlESNGjWoVauWcr5WrVokJSUVKY7v3LlD48aNi/Snq6ur/P3ixYtERERQs2ZNbGxs2LhxIzVq1GD58uWEhYUxbNgw9uzZQ5cuXTh+/Dg9e/aUwlgIIYQog3/8fy1v3LiBSqVSjrt27YqjoyPnz59n69ataGtrk5qaqlwv2JdrYWHBzz//TJ8+fWjRokWxwhhg1apVmJiY0KtXLyCvyJk3bx65ubnEx8fTuXNnDAwMaNmyJXp6ehgZGdG4cWP09fUxNDTkyZMnZZ5HwerjmTNnOH36NNHR0QBkZmaSlZUFQMeOHQGoW7cuqampXL16lXbt2gFgaWlJpUqVABgyZAgfffQRb7/9NkOGDKFSpUqcO3cONzc3IG/Fs/BK84teFkNBnC/Kzc1l5syZdO7cmS5dugBw/fr1IlsEgoKCuHjxIjNmzGD37t1oaWmVOT8FCr4NaNiwoXKudevWaGlpYWRkRIsWLdDR0aF27dpK/A0bNqRmzZrKSq6xsTFPnz4t9fW5evUq9erVIyYmBhsbmzLHptFoXvm8lpYWBw4cYPPmzTx9+pQBAwYwZMgQGjRoQM2aNXn48CG3bt1i6tSpADx79oyaNWsyePBgPv/8c7KzswkPD+edd94pc5x/hJFR1b9knP8PJBflS/JZ/iSn5UvyWb5eZz7/8cVxSXuOf/zxR9LS0ggMDCQ1NRVbW1vlWuGCrODvJRXGANWqVePo0aOkpKRQs2ZNXF1dWbNmDc2aNcPDw0O5r/CK3e9dvStYNdTV1WXSpEkMGTKk2D2F96xqNBo0Gg3a2v/7zaVarQbgww8/ZOjQoezbt49x48bh7+9P5cqV2bx5c5kK0pfFUHh1s7A5c+bQqFEj5QeGiYmJ1K1bF4DY2FgMDQ0xMTGhVatW5ObmkpycjKGh4W/G8qIjR47QuXPnIudKy39BUVo4b7/1+qSnp+Pt7c2WLVuYPHkysbGxtG7dusR7a9WqVeSD1/3796lTpw516tThxo0bxc4X1rBhQy5evMh///tf+vfvT//+/ZW96FD0/VCnTp0S99V369aN48ePc+XKFeVD0p8tKansH/j+yYyMqkouypHks/xJTsuX5LN8/RX5fFnx/Y9+WkVpUlJSqF+/Ptra2hw4cEBZ9QQ4deoUAGfPnqVp06Yv7Wfs2LE4Ojri6ekJ5BVOJiYmPH78mKioKLKzs8s9dktLS8LDwwF49OgRK1euLPXeJk2aEBsbC0B0dDRZWVmo1Wq8vLwwMjJiwoQJtG3bljt37tCyZUt++uknAEJDQzl+/DjwvwJSW1ub3NzcV44BYPfu3ejq6uLs7KycO3HiBG+88QaQl/MNGzYA8PDhQ2X18/c4f/48LVu2/F1ty2LFihXY29tTq1Yt5s6di4eHh/Kh40W6uro0bdpUeU/t37+fHj160LlzZw4fPkxWVhb379/nwYMHNG/evEjb8ePHs2TJEp49ewbkreafPHmy2Ae16tWrA3mr2ZC3V/nSpUsADBs2jK+//lrJsxBCCCF+2z9+5bgkAwYMYPLkyZw9e5YRI0ZQt25dfHx8gLxiz9HRkcePH/P1119z69atl/Y1YsQI9u7dS3h4OGPGjGH06NE0btwYR0dHvL29i/2Y7I8aNGgQkZGR2NnZkZub+9JHvfXs2ZPt27fj4OBAy5YtMTY2RltbGwMDA0aNGkXVqlVp0KABrVq1Yu7cubi5ubF27VoqVqzIF198AUCrVq2wtbVly5YtZGdn4+zszMqVK8scA0BgYCCZmZnK9pZmzZqRkZHBxIkTgby9xnPnzmXMmDFkZGQwf/78IiveLzp8+DDr16/n+vXrXLhwAT8/P6W4TkpK+l0rzmVx5swZLly4oPzY0MLCAjMzM4KCgjA1NS0xJldXV+bPn49arcbS0pKuXbsC8O677+Lg4ICWlhbu7u7F5jtgwACeP3+Ovb09lStXJiMjgx49ejBlypQij8KDvCdizJkzR1lFHjVqFJC3nSQtLY2hQ4f+KfkQQggh/om0NKVteBRC/L9248YNFi5cyMaNG3/z3qEuu8plzA2z+5ZLP//fyVes5UvyWf4kp+VL8lm+Xve2in/lyrH4P/buPKyqeu3/+HszOYAW6EbQTMnDTzwOaEdTsTR6MIdHzQIVlK2YkHJE0CggFSXIqYNT6skhUZkcIxwyhwhLU9EEURBRHAoQFQU0BGWQ3x/gqi1D2Nnqc+x+XZdX7LXX+q573Zuu67O/+7sX4lm3ceNGtmzZwvz58592KUIIIcR/FQnHQjyDXFxcqt1STwghhBB/7C/5hTwhhBBCCCFqIjPHQgh2LnxL1ssJIYQQyMyxEEIIIYQQCgnHQgghhBBCVJFwLIQQQgghRBUJx0IIIYQQQlSRcCyEEEIIIUQVCcdCCCGEEEJUkXAshBBCCCFElXrf57ioqIhLly6hUqmwsrKiUaNGj7MuIYQQQgghnrh6heNvv/2WoKAgLCwsuH//Pjdu3CAkJIR+/fo97vqEEEIIIYR4YuoVjr/44gt27NiBmZkZANeuXcPHx0fCsRBCCCGEeKbUa82xoaGhEowBWrRogaGh4WMrSgghhBBCiKehXjPHxsbGhIWFYWdnkItCnAAAIABJREFUB8ChQ4cwNjZ+rIUJIYQQQgjxpNUrHM+ZM4elS5eyY8cOVCoVXbt2Ze7cuY+7NiGEEEIIIZ6oeoXjo0ePEhwcrLVt48aNuLi4PJaihBBCCCGEeBrqDMdnzpwhNTWVsLAwiouLle1lZWWsWLFCwrEQQgghhHim1BmOGzRowM2bN/n11185ceKEsl2lUuHn5/fYixNCCCGEEOJJqjMct2vXjnbt2tGrVy+6du36pGoSQjxhQ32362ScsIA3dDKOEEII8bTUa83xp59+ikqlqrY9KipK5wUJIYQQQgjxtNQrHE+dOlX5ubS0lKNHj9K4cePHVpQQQgghhBBPQ73C8SuvvKL1uE+fPnh4eDyWgoQQQgghhHha6hWOMzMztR7n5ORw6dKlx1KQEEIIIYQQT0u9/nz0uHHjlH9ubm7MmTMHLy+vx12bzu3atYuOHTuSl5dX4/ORkZEsW7ZMJ+fas2ePTsYBCAkJYevWrcrjoKAgPv30U+Xxhg0bWLhwYb3G6tmz5yOf/88c83tXrlzh1KlTf+rY8PBwOnbsyJ07d5RtHTt2RKPRKP/Ky8trPPbgwYO0b98e+HM9DAgIYMKECVrb4uPjad++PVlZWQCcO3cOBwcHIiMjtY4bOnSoUt+BAwe0xnj//fcJCAgA4Nq1a0yYMAGNRsOYMWNISUmpdh2/v14XFxe8vb0pLCystWe/d+fOHd54Q74kJ4QQQtRXvWaOv/vuu8ddxxOxa9cuWrduzd69ex/7PZpXr17NwIEDdTJWz549iYuLY8SIEQBcuHABPb3f3tecOHGCkSNH6uRcj8PRo0cpKiqiS5cuj3RcbGwsN2/exNzcXGu7iYkJERERdR577949Vq9ejVqtBv58D7OyssjLy8PMzAyA3bt307p1awCKiooICQmhd+/e1Y57//33sbe3r7b9xx9/5JdffuFvf/sbAOvXr6d///44OzuTmJjI4sWLWbt2bZ3Xu2zZMjZs2MDkyZPr7IEQQgghHl2d4fijjz6q8+B58+bptJjHqaCggFOnTjF37ly++OILJRwfOXKEuXPn0rx5c9RqNa1bt2by5Mm4ubnRo0cP7t69y+DBg9m/fz+fffYZP/30E+Xl5bi6ujJkyBACAgIwNzcnNTWVK1euEBoaypEjR0hPT8fLywuNRkNUVBSfffYZUBnSEhIS0Gg0WFtbA5VBavr06dy6dYvy8nJmzpyJjY2NUnuPHj2UWc6CggKMjIwoKSmhuLiYRo0akZyczPz580lPTyc4OBg9PT2MjY2VbWFhYRQVFeHv76+MmZaWxscff8zatWtZvHgxKSkplJeX4+LiwjvvvPOH/Tx79iwff/wxBgYG6OnpsXTpUgoLC/Hx8aFt27ZcvnyZzp074+3tzfLlyzEwMMDS0pIXXnihxhrXrFmDkZERV65cYcCAAXh6euLg4ICJiQk7d+585Nd75cqVjB49mn/961+P1MOHvfrqq3zzzTeMGTOGu3fvcvnyZSwtLQEwMjJizZo1rFmzpl41lZSU8Pnnn+Pp6cn+/fsBMDU1paCgAIDbt29jamr6h+N06dKFr7/+GoB9+/YRFhaGgYEBnTp1IiAggMLCQqZMmcK9e/f4xz/+Ua/ahBBCCFGpznD88ssvA3Dy5Eny8/Pp2bMn9+/f58iRI7zwwgtPpEBd2bNnD6+//jqvvfYaM2fO5Nq1a7Ro0YKFCxfyr3/9CxsbGzw8PGjdujX9+/fnu+++o0ePHvz444/06dOHpKQksrOziYqKoqSkhLfffhsHBwegMvSsXbuWjRs3Ehsby4wZM1izZg3Lly8nISGh1pqsra1xcXFhxYoVvPbaa4wYMYKMjAzmzJnDunXrlP1MTU0xNjbm6tWrnDlzhq5du1JcXExSUhIWFha0bNmSxo0bM2fOHPz8/LC1tWXt2rWEh4fTs2dPzp07x969ezEyMgIgLy+P2bNns2TJEkpLSzlw4ADffvstpaWlfPXVV/Xq582bNwkMDOTvf/87S5cuZefOndjb25Oens7y5cuxsLDAycmJ69ev8/bbb2Nqasr//M//MHbs2BprTElJIS4uDgMDAwYNGoSzs3OtQbGkpARfX1+ys7MZMGAA48eP13r+0qVLnD17Fh8fHyUc17eHD3vzzTdZunQpY8aM4cCBA9jZ2ZGYmAiAgYEBBgY1/y8UGRnJunXraNasGYGBgZiZmbFq1SpcXFwwMTFR9nNzc8PJyYnY2FgKCwvZuHFjnX2vqKhg3759/P3vf+fOnTt8/vnnbN68GSMjI3x8fDhx4gRnz57F2tqa6dOns3v3biVIPwlqdZMndq7/66QXuiX91D3pqW5JP3XrafazznD84CPo/fv3s3r1amW7m5vbf91Hurt27eKf//wn+vr6DBw4kN27dzN+/Hiys7OVWdoePXpw79493njjDdauXYu/vz9xcXEMHjyYxMREkpOT0Wg0ANy/f5/c3FwAunfvDoCFhcUjra19sMwgKSmJvLw8duzYAaD1p7of6NmzJ8eOHePs2bO89tprFBUV8dNPP2FpaamsCb5w4QK2trbK/suXL6dnz560b99eCcYVFRVMmzYNd3d3WrZsCUDbtm3x9PRk4MCBDB8+vF61N2vWjNDQUO7evcv169cZOnSoMtaDmVVbW1suXryodVxtNdra2mJsbAxUvmnIzMysNRz7+fkxbNgwVCoVrq6udO/enc6dOyvPz5s3j5kzZ/6pHj6sVatWlJaWcuXKFXbv3o2np6cSjmvz1ltv8fzzz9OhQwdWr17N8uXLGTt2LCkpKUyZMkXrDdMXX3zBoEGD8PT0JD4+ngULFrB8+XKt8QoLC5Xfu4yMDIYOHYqrq6vyacWDddG//vorV65c4cKFC/To0QOofqeZxy0399cner7/q9TqJtILHZJ+6p70VLekn7r1JPpZV/iu15rjnJwcbt++TdOmTYHKL/k8fAeL/8uuXr2qfGyuUqm4e/cuTZo0Yfz48VrrTisqKgBo2rQp5ubmXLx4kaSkJIKDg8nIyMDJyYmJEydWG19fX7/aGA88/MdTysrKlJ8NDQ2V/wYGBtKtW7dar6Fnz54cPHiQc+fO4eXlxb1794iOjiY7O7vGQFtaWqpc24NgDJVBq3379mzatIk333wTqAxoqamp7Nq1i+3btxMWFlZrHQ/MmTMHDw8P+vbty9q1aykqKgIq3zT8vhc1/fGYmmp8+Li6/H69eK9evTh37pwSjq9du8bFixf54IMPALh+/Tqurq5ERkY+cg8fGDBgAF999RWXLl2iQ4cOddYGaK1BfuONNwgKCuLAgQNcuXKFkSNHUlhYSF5eHmvWrCExMVG5j3ifPn34+OOPq433+zXHCxYsoEWLFhgYGGBoaEinTp2qrVFOTEyssa9CCCGE+GP1uluFs7Mz/fv3x9HREScnJxwcHHB0dHzctenMrl27GDNmDDt27GD79u3s2bOHW7du8csvv9CiRQsuXrxIRUUFx44dU47p378/K1eupGvXrhgYGNClSxfi4+O5f/8+9+7dIyQkpM5zPgh4JiYmXL9+Hahcp/v7uy48YGtry7fffgtUzgz+fknFAz169ODkyZPo6enRuHFjTE1NuXPnDunp6cryF2tra5KSkgA4fvw4nTp1qjZOkyZNmD59Omq1mi1btpCVlaXcEcLf319Z//pHCgoKePHFFykpKeH777+ntLQUgF9++YXr169z//59kpOT+dvf/oZKpVLeFNRW45kzZyguLubevXtkZGTQtm3bGs978eJFfH19qaiooKysjMTERGXtNkCLFi349ttv2bJlC1u2bMHc3Fy5k0R9eliTAQMGEB4eTt++fevVmylTpihvHhMSErC2tsbNzY2dO3eyZcsWZs+ezeuvv46Hhwdt2rQhOTkZgFOnTtGmTZs6x/7nP/9JVFQU169fx8rKigsXLnDz5k0APvvsM65du4aVlZVy14u6lvUIIYQQorp6zRyPGTOGt956i59//pmKigpefPFFZRb5v8HXX3/NggULlMcqlYrhw4fz9ddfM3XqVHx8fGjZsiUWFhbKPg4ODnzyySesWLECqFx/3bNnT0aNGkVFRQWjR4+u85wdOnTAycmJLVu20LhxY5ydnenWrRutWrWqtq+rqysfffQRo0eP5v79+8yYMaPaPk2bNkVPT4+OHTsq26ytrbl8+TINGjQAYObMmXz88ceoVCqee+455s2bR2pqao31TZ8+nVGjRinrqXfv3o2hoWGNb3p+/7E+VC6rcXV1ZfLkybRu3RqNRkNwcDCDBw/GysqKxYsXk5GRwcsvv4y1tTXXr1/H398fMzOzWmts164d06dP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\n",
            "text/plain": [
              "<Figure size 576x396 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qFQBaeXNcMd4",
        "colab_type": "code",
        "outputId": "bbe89a72-81a8-4a44-c93c-6b01de01621a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 388
        }
      },
      "source": [
        "df.groupby(df[\"Data Venda\"].dt.year)[\"lucro\"].sum().plot.bar(title=\"Lucro x Ano\")\n",
        "plt.xlabel(\"Ano\")\n",
        "plt.ylabel(\"Receita\");"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 576x396 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4-FPJ5dP5saX",
        "colab_type": "code",
        "outputId": "3f945085-2546-4643-86b3-bbb2f0f9d235",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        }
      },
      "source": [
        "df.groupby(df[\"Data Venda\"].dt.year)[\"lucro\"].sum()"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Data Venda\n",
              "2008           1,920,077.71\n",
              "2009           1,577,745.38\n",
              "Name: lucro, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qEjCs7y77966",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Selecionando apenas as vendas de 2009\n",
        "df_2009 = df[df[\"Data Venda\"].dt.year == 2009]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GiL4JRnU_LSf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 496
        },
        "outputId": "f55f66df-5bd7-408b-9113-c7bf694fd2fb"
      },
      "source": [
        "df_2009.head()"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Data Envio</th>\n",
              "      <th>ID Loja</th>\n",
              "      <th>ID Produto</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>No. Venda</th>\n",
              "      <th>Custo Unitário</th>\n",
              "      <th>Preço Unitário</th>\n",
              "      <th>Quantidade</th>\n",
              "      <th>Valor Desconto</th>\n",
              "      <th>Valor Venda</th>\n",
              "      <th>Produto</th>\n",
              "      <th>Fabricante</th>\n",
              "      <th>Marca</th>\n",
              "      <th>Classe</th>\n",
              "      <th>Cor</th>\n",
              "      <th>custo</th>\n",
              "      <th>lucro</th>\n",
              "      <th>Tempo_envio</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>2009-05-02</td>\n",
              "      <td>2009-05-14</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18938</td>\n",
              "      <td>200905023CS847</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.00</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4,548.00</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2,091.48</td>\n",
              "      <td>2,456.52</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>2009-05-16</td>\n",
              "      <td>2009-05-27</td>\n",
              "      <td>306</td>\n",
              "      <td>384</td>\n",
              "      <td>19067</td>\n",
              "      <td>200905163CS746</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.00</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4,548.00</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2,091.48</td>\n",
              "      <td>2,456.52</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>2009-05-31</td>\n",
              "      <td>2009-06-12</td>\n",
              "      <td>306</td>\n",
              "      <td>384</td>\n",
              "      <td>19068</td>\n",
              "      <td>200905313CS748</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.00</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4,548.00</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2,091.48</td>\n",
              "      <td>2,456.52</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>2009-06-28</td>\n",
              "      <td>2009-07-11</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18959</td>\n",
              "      <td>200906283CS870</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.00</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4,548.00</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2,091.48</td>\n",
              "      <td>2,456.52</td>\n",
              "      <td>13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>2009-07-08</td>\n",
              "      <td>2009-07-12</td>\n",
              "      <td>306</td>\n",
              "      <td>384</td>\n",
              "      <td>19070</td>\n",
              "      <td>200907083CS757</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.00</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4,548.00</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2,091.48</td>\n",
              "      <td>2,456.52</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Data Venda Data Envio  ...                lucro  Tempo_envio\n",
              "11 2009-05-02 2009-05-14  ...             2,456.52           12\n",
              "12 2009-05-16 2009-05-27  ...             2,456.52           11\n",
              "13 2009-05-31 2009-06-12  ...             2,456.52           12\n",
              "14 2009-06-28 2009-07-11  ...             2,456.52           13\n",
              "15 2009-07-08 2009-07-12  ...             2,456.52            4\n",
              "\n",
              "[5 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xaH-Ym6h_SG9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 376
        },
        "outputId": "1ea0cbdf-ecea-4722-e6c4-9e0557b931c1"
      },
      "source": [
        "df_2009.groupby(df_2009[\"Data Venda\"].dt.month)[\"lucro\"].sum().plot(title=\"Lucro x Mês\")\n",
        "plt.xlabel(\"Mês\")\n",
        "plt.ylabel(\"Lucro\");"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 576x396 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8HDLr3pp_hqf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 376
        },
        "outputId": "e476ce16-0d5f-4bf6-c5c5-7cec1e4ec576"
      },
      "source": [
        "df_2009.groupby(\"Marca\")[\"lucro\"].sum().plot.bar(title=\"Lucro x Marca\")\n",
        "plt.xlabel(\"Marca\")\n",
        "plt.ylabel(\"Lucro\")\n",
        "plt.xticks(rotation='horizontal');"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAe8AAAFnCAYAAACPasF4AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAgAElEQVR4nO3de1xUdf7H8fcMoIUSC7tDXn/r5WdimK6ulzXaNQkvqVtmbqCCdnHbLN1uGoYaKYJamT+vm1vWVl7CJbp5Y8tsK0OJ8vKApNISBUtBgeQiAp7fH/6cXyxoVBzxO76ej0ePOHNmznyAIy/OmWHGYVmWJQAAYAxnYw8AAAB+HOINAIBhiDcAAIYh3gAAGIZ4AwBgGOINAIBhiDdwEencubO+/fbbxh7jB+3YsUOdO3fWqlWraq0bNGiQoqOjG2Eq4NJBvAH8JC1bttT69etrXLZnzx6dOnWqkSYCLh3EGzDAtGnTtHz58jqXMzMzNXLkSA0ePFhRUVE6dOiQJCksLExLly7V4MGDdfjwYR0+fFh33XWXBg8erOHDh+v111+vdT95eXm69tpr3Uf/b731lm677TadPn261nXbtm2roqIi5ebmui/buHGjQkND3cunT5/WrFmzNHjwYIWFhWnq1KmqrKx0fw5z587VH//4R23atEknT57UI488orCwMN1444164403JEnl5eV64IEH3NuYP3/+z/1yAsYj3oDhHnroId1///1KTU1VeHi44uPj3euOHDmi1NRUtWrVSjNnzlSfPn2UmpqqFStWaM6cOTXCK0mtW7fW3XffrSeffFJlZWVauHCh4uPj5XTW/aNiyJAh2rBhgyTJsixt2bJFAwYMcK9/++23lZGRofXr12vTpk3KysrSxo0b3evT0tKUnJysG2+8Uc8//7wqKyv17rvv6oUXXlB8fLyOHDmitWvXqrS0VJs3b9Zrr72mlJQUZWRkNOSXEDCOcfH+4osvFB4eXudjbd+XnZ2tkSNHauTIkVq2bNkFmg64sL7++msVFhaqf//+kqSoqCgtWbLEvf7666+XJFVWVuqjjz7SmDFjJJ2JdN++fbV9+/Za24yOjtaBAwf04IMPatiwYercufM573/YsGHuU+cZGRnq1KmT/Pz83OsHDx6sV199VT4+PmratKmuueYa95kBSerXr5+aNm0qSXr//fc1bNgwSVKLFi3073//W1deeaXuvPNOLV++XA6HQ/7+/urUqVOtXzqAS41R8S4rK1N8fLz69ev3g9edOXOm4uPjlZycrP3796u8vPwCTAhcWIWFhTVi6e3t7Y6hJPn7+0uSioqKZFlWjeteccUVOn78eK1tenl5KSIiQu+9955uu+22895/p06dJJ35pXrDhg0aOnRojfXHjx9XTEyMBg8erCFDhmjLli36/tspnJ2vrs+lWbNmkqQDBw5o8uTJGjRokIYMGaLMzMw6T+MDlxKj4t2kSRM9++yzCgoKcl+2b98+jRs3TuPHj9e9996r7777TgUFBSorK1NISIicTqeefvppXX755Y04OfDzOJ3OGsEqLi6WJAUEBKioqMi9rrKyss6j0oCAADmdTvftpDNB/+Uvf1nrumVlZXruuecUHR2tJ5988gdnGzZsmDZt2qT3339fYWFhNdYtXLhQ3t7eeuutt7R582b3GYK6BAQEqLCw0L387bffqry8XLNnz1anTp20adMmbd68WcHBwT84E+DpjIq3t7e3LrvsshqXxcfHa/bs2XrxxRcVGhqq1atXKy8vT/7+/po2bZoiIyP1j3/8o3EGBhqIy+VSdna2JOnQoUP69NNPJUnt2rVTixYt9K9//UuSlJycrMcee6zW7b29vXXdddcpKSlJknTw4EFlZGTo2muvrXXdJUuWaODAgXr00UeVk5OjrVu3nne2YcOGad26dbrmmmvk6+tbY92xY8d01VVXqUmTJsrOztbOnTtVVlZW53bCwsL0+uuvy7Is5efna8SIESosLNSxY8fUpUsXeXl5adu2bcrJyTnnNoBLhXdjD/Bz7dmzRzNnzpQknTp1Stdcc40sy1Jubq6WLVumyy67TBEREQoNDXWf4gMuZtHR0fLy8nIvz5kzR7fddpsmTZqkQYMG6eqrr9bgwYMlSQ6HQ4sWLdLUqVP19NNPy+Vyae7cuXVud9asWZoxY4ZSUlLk4+OjOXPmqGXLljWuk52drdTUVL311lvy8vLSzJkzNXXqVPXp08d9Gvs/tW3bVq1bt651ylyS7rzzTsXExCglJUW9evVSTEyMpk+frm7dutW67u23366cnBwNGDBAl112mWJiYtSqVStNnDhRc+fO1fLly3XDDTdo0qRJWrx4sbp06aLf/va39f66Ap7EYeL7eS9Z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+PHjda5ftWqVlixZ0iD3tXnz5gbZjiTFx8frn//8p3v58ccf1xNPPOFefvHFF7VgwYJ6batv374NNhca1oEDB3T33Xdr1KhRGjlypOLj43Xq1KkftY2G3O9gptzcXPXo0UPR0dHu//7zVTPPio6O1hdffHHe7U2cOLHe10XdiPfPtH79erVt29b9zHo7/f3vf2+wbfXt21cZGRnu5f379ysrK8u9/MknnxBlw1VXV2vy5MmaMGGCkpOT9eqrr0rSj34vgYbc72Cu9u3b6+WXX3b/N3369J+8rb/97W8NONml6YK9SIsnKioq0p49e5SYmKjnnntOo0ePlnTmpWETExP1q1/9Si6XS23bttV9992n22+/Xb1799bJkyc1dOhQvf3221q8eLEyMjJUXV2tqKgoDR8+XNOmTVNQUJCysrJ0+PBhPfXUU0pLS9Pnn3+uSZMmKTo6WqtXr9bixYslnQnxjh07FB0drU6dOkmSHnroIcXGxqq4uFjV1dWaMWOGgoOD3bP37t3bfaRdVFSkJk2a6NSpUyovL9fll1+u3bt3a968efr88881e/ZsOZ1ONWvWzH3Z888/r7KyMsXExLi3uXfvXs2aNUsrV67UwoULlZmZqerqao0ePVojR468UN8W/J9t27apQ4cO6tOnjyTJ4XBo6tSpcjqdevHFF7Vx40ZJ0g033KC77777B/e7pUuX6oknntCnn36q6upqjR07ViNGjNDrr7+uVatWycfHR8HBwYqLi6tzv/nFL37RmF8ONLCqqirFxMToyJEjKisr0+TJkzVgwABJUnJysvbu3avy8nItWrRIubm5NX5m3HXXXdqxY4d7WyUlJbrjjjuUmJio/Px8LVq0SD4+Prriiiv0P//zP9q5c6deeukleXl56bPPPtM999yjDz74QHv37tUjjzzifinuS4qFn2zt2rXWo48+alVVVVmhoaHWt99+a1mWZd16663W3r17LcuyrAkTJliLFy+2XnvtNWvevHmWZVnWO++8Y82YMcP6+OOPrYcfftiyLMuqqKiwhg4dapWXl1sxMTHW3LlzLcuyrDVr1lhz5syxLMuy+vTpY1mWZW3fvt2aPHmye46zl0dFRVlr1qyxLMuyli5daq1bt86yLMv68ssvrdtvv73W/DfddJP1zTffWFu2bLEWL15szZ8/39q2bZu1f/9+KzIy0rIs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AJeQoKAgVVRU6Msvv1SnTp1UXl6uTz75xP065IsWLVJaWpqkM69v/uSTT8rHx0c9e/bUqFGjdPr0ac2YMUPLly/Xli1b5HQ6dfPNNysqKkoZGRl66qmn1KRJE508eVJxcXE1XgAIQMPhyBu4xNx8883u9/ZOTU3VH/7wBzmdTlVXV+vyyy/XmjVr9Morr+jEiRP68MMPJUllZWXq37+/ZsyYoYyMDL333ntat26d1qxZow8//FDfffedioqK9Pjjj+ull17SuHHjtGLFisb8NAGPxpE3cIm58cYbdcstt2jKlCl67bXXNGXKFK1evVpeXl5yOp0aM2aMvL299dVXX6mwsFDSmdc3P/t697t379Zvf/tbeXl5ycvLS88884wk6Ve/+pWeeOIJVVRU6MSJE/L392+0zxHwdMQbuMQEBgbq6quvVnJysvLz83XNNddIkj799FO9+eabevXVV+Xr66u//vWvNW539h3rHA5HrXcck6RHHnlEs2bNUr9+/bR161beSQ6wEafNgUvQzTffrIULF2rYsGHuyzp27KjWrVvL19dXeXl52rVrV413ijqrR48eSktLU2VlpaqqqhQdHa2jR4+qoKBAnTp1UnV1tTZv3lznbQE0DOINXILCwsJkWZZuuukm92U+Pj4qKSnR6NGjtWLFCk2ePFnPPPOMvv766xq37dGjhwYNGqSxY8dqzJgxCg8PV1BQkP785z9r/Pjxuueee3TLLbfom2++0T/+8Y8L/JkBlwbeVQwAAMNw5A0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhiHeAAAYhngDAGCY/wUmRk5LfbwzXwAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 576x396 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xguSC8ya_mr7",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 376
        },
        "outputId": "bec6125e-6b51-4aac-b9df-d6826c26afdc"
      },
      "source": [
        "df_2009.groupby(\"Classe\")[\"lucro\"].sum().plot.bar(title=\"Lucro x Classe\")\n",
        "plt.xlabel(\"Classe\")\n",
        "plt.ylabel(\"Lucro\")\n",
        "plt.xticks(rotation='horizontal');"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAe8AAAFnCAYAAACPasF4AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAgAElEQVR4nO3dfVSUdf7/8dcMI2pKCjWTCrqhJ7vB7GSmq1gq4k1m52fFCoU3rVYn11S6FS1FxfEm71bJTmZmrfflIYs00U1XW8WbrDSsvDtFigmDIgpo3s3vD8/OV1IM04vxMz4f5+zJ62Yu3sNZ5sl1zTBj83q9XgEAAGPY/T0AAAC4PMQbAADDEG8AAAxDvAEAMAzxBgDAMMQbAADDEG/gGnH77bfr4MGD/h6jQo4dO6bRo0erU6dO6ty5s7p27ar33ntP//vL05iYGH311Vd+nhIIXA5/DwDALGfPntUzzzyjRo0aKSMjQ1WrVtXBgwc1YMAAFRUV6YUXXvD3iEDA48wbuMYlJyfrrbfeuuhydna2HnvsMXXu3Fk9e/bUvn37JJ07833zzTfVuXNnHThwQAcOHFC/fv3UuXNndevWTUuXLr3g6+Tm5qp169a+s/+MjAz16NFDZ8+eLbPfunXrlJeXp5EjR6pq1aqSpDp16mjq1Knq0KHDBcf96KOP9NBDD6lTp05KTExUbm6uJCkvL099+vRR165dFRsbq6lTp15yvdfr9d2n9u3ba8yYMTpz5swVfW8BUxFvwGAvvviiBg8erMzMTMXGxio1NdW3LS8vT5mZmapXr56GDx+uFi1aKDMzUzNnztSYMWO0f//+MscKDw/Xs88+q4kTJ6q0tFRTp05Vamqq7PayDxObN29WdHS0qlSpUmZ9gwYN1LRp0zLrDh06pNGjR2vOnDlauXKlGjRo4PvF4/3339f999+v5cuXKyMjQ/v27VN+fn656z/55BOtWLFCS5Ys0apVq7Rv3z4tXLjwan47AWMYF+9du3YpNjZW8+bNu+R+P/74ox577DE99thjmjFjRiVNB1Sen376SYWFhWrbtq0kqWfPnkpLS/Ntb9eunSTp1KlT2rBhg5588klJ5yLdsmVLbdy48YJj9urVSz///LNeeOEFPfzww7r99tsv2KeoqEg33XRThWa86aabtHXrVtWpU0eS1Lx5c9/VgZtuukn//e9/9dVXXyk4OFhTpkyRy+Uqd/2aNWv0+OOPKyQkRA6HQ3/729+0cuXKin/DgABi1HPepaWlSk1NVatWrf5w3+HDhys1NVV33nmnXn75ZR0/flzVq1evhCmBylFYWKiQkBDfssPhkMPxfz/StWrVkiQdOXJEXq+3zL433nijDh8+fMExg4KCFB8fr+HDh+v111+/6NcNDQ1Vfn5+hWY8c+aMpk+frtWrV+vMmTMqKSlRZGSkJOmpp57S2bNnNWrUKOXn5ysxMVEDBw4sd/2xY8c0e/ZsLV682HfssLCwCs0BBBqjzryDg4M1a9YsuVwu37o9e/aod+/e6tOnj/7xj3/o6NGjKigoUGlpqaKiomS32zVlyhTCDWPZ7fYyzzsXFRVJOhfRI0eO+LadOnXqgkvh/9vPbrf7biedC/rFzp5LS0v17rvvqlevXpo4ceJF52nZsqXWrVunEydOlFn/yy+/aM6cOWXWLV++XKtXr9a8efOUmZmpQYMG+bY5HA49++yzysjI0KJFi/Tpp59qw4YN5a53uVx67rnntGLFCq1YsUKrVq3yhRy43hgVb4fDoWrVqpVZl5qaqtGjR+uDDz5QdHS05s+fr9zcXNWqVUvJyclKSEjQ+++/75+BgavA6XTqxx9/lCTt27dPX3/9tSTp1ltvVZ06dXyXjpcsWaIRI0ZccHuHw6E2bdr4QvfLL7/oq6++UuvWrS/YNy0tTR07dtTQoUOVk5OjNWvWXLBPmzZt1LBhQ7366qsqLi6WJB08eFBJSUk6ffp0mX0PHTqk8PBwhYWFqbCwUJ9//rlKSkokSSNGjND69eslnXu+/Oabb5bNZit3fYcOHfTJJ5/o+PHjkqRFixbp448/vszvJhAYjLpsfjHbt2/X8OHDJUknT57U3XffLa/Xq/3792vGjBmqVq2a4uPjFR0drdtuu83P0wKX1qtXLwUFBfmWx4wZox49euj5559Xp06ddNddd6lz586SJJvNpmnTpumVV17RlClT5HQ6NW7cuIsed9SoUXr99deVnp6uKlWqaMyYMapbt26ZfX788UdlZmYqIyNDQUFBGj58uF555RW1aNFCNWrU8O1ns9n09ttva+rUqerevbscDoeqV6+uxMRExcXFlTlmt27dtGzZMnXs2FH169dXUlKS+vfvr/HjxyshIUEjRoxQamqqvF6vYmJi1KpVK9WuXfui6yVp9+7devTRRyWdC7vb7b7ybzpgIJuJn+edlpam0NBQ9ezZU61bt9b69etls9l82/ft26eRI0dq9uzZks49cN1///3q2rWrv0YGAOCqMeqy+cXccccdWrdunSRp2bJlysrKUv369VVSUuJ7PvCHH35Qw4YN/TwpAABXh1Fn3tnZ2ZowYYJyc3PlcDh0yy23KCkpSZMnT5bdblfVqlU1efJk1a5dW9u2bdOYMWNks9n0wAMPaODAgf4eHwCAq8KoeAMAgAC4bA4AwPWGeAMAYBhj/lTM4znm7xFwBUJDb1BhYam/xwCuO/zsmc3pDLnoes68USkcjqA/3gnAVcfPXmAi3gAAGIZ4AwBgGOINAIBhiDcAAIYh3gAAGIZ4AwBgGOINAIBhiDcAAIYh3gAAGIZ4AwBgGOINAIBhiDcAAIYx5lPFAMAKfcev9vcIuALvJcf4ewS/4MwbAADDEG8AAAxDvAEAMIyl8d61a5diY2M1b968cveZPHmyevXqZeUYAAAEFMviXVpaqtTUVLVq1arcffbs2aMtW7ZYNQIAAAHJsngHBwdr1qxZcrlc5e4zfvx4vfDCC1aNAABAQLLsT8UcDoccjvIPn56erhYtWig8PNyqEQAACEh++TvvI0eOKD09XXPmzFFeXl6FbhMaeoMcjiCLJ4OVnM4Qf48AIMBcr48rfon3xo0bdfjwYSUmJurkyZP65ZdfNHbsWA0bNqzc2xQWllbihLjanM4QeTzH/D0GgAAT6I8r5f1y4pd4d+nSRV26dJEk7d+/X0OHDr1kuAEAwP+xLN7Z2dmaMGGCcnNz5XA4lJmZqZiYGEVERKhjx45WfVkAAAKeZfFu0qSJ5s6d+4f7RUREVGg/AABwDu+wBgCAYYg3AACGId4AABiGeAMAYBjiDQCAYYg3AACGId4AABiGeAMAYBjiDQCAYYg3AACGId4AABiGeAMAYBjiDQCAYYg3AACGId4AABiGeAMAYBjiDQCAYYg3AACGId4AABiGeAMAYBjiDQCAYYg3AACGId4AABiGeAMAYBjiDQCAYYg3AACGId4AABiGeAMAYBjiDQCAYYg3AACGId4AABjG0njv2rVLsbGxmjdv3gXbNm7cqB49eighIUFDhw7V2bNnrRwFAICAYVm8S0tLlZqaqlatWl10+4gRIzR9+nQtWrRIJSUl+vLLL60aBQCAgGJZvIODgzVr1iy5XK6Lbk9PT1edOnUkSWFhYSosLLRqFAAAAorDsgM7HHI4yj98zZo1JUn5+flav369Bg8efMnjhYbeIIcj6KrOiMrldIb4ewQAAeZ6fVyxLN4VcejQIT333HNKSUlRaGjoJfctLCytpKlgBaczRB7PMX+PASDABPrjSnm/nPjt1ebFxcV65plnlJSUpDZt2vhrDAAAjOO3eI8fP159+vTRgw8+6K8RAAAwkmWXzbOzszVhwgTl5ubK4XAoMzNTMTExioiIUJs2bbR06VLl5ORoyZIlkqRu3bopPj7eqnEAAAgYlsW7SZMmmjt3brnbs7OzrfrSAAAENN5hDQAAwxBvAAAMQ7wBADAM8QYAwDDEGwAAwxBvAAAMQ7wBADAM8QYAwDDEGwAAwxBvAAAMQ7wBADAM8QYAwDDEGwAAwxBvAAAMQ7wBADAM8QYAwDDEGwAAwxBvAAAMQ7wBADAM8QYAwDDEGwAAwxBvAAAMQ7wBADAM8QYAwDDEGwAAwxBvAAAMQ7wBADAM8QYAwDDEGwAAwxBvAAAMY2m8d+3apdjYWM2bN++CbRs2bFBcXJzi4+M1Y8YMK8cAACCgWBbv0tJSpaamqlWrVhfdPmbMGKWlpWnhwoVav3699uzZY9UoAAAEFMviHRwcrFmzZsnlcl2wbd++fapVq5bq1q0ru92utm3bKisry6pRAAAIKJbF2+FwqFq1ahfd5vF4FBYW5lsOCwuTx+OxahQAAAKKw98DVFRo6A1yOIL8PQaugNMZ4u8RAASY6/VxxS/xdrlcKigo8C3n5eVd9PL6+QoLS60eCxZyOkPk8Rzz9xgAAkygP66U98uJX/5ULCIiQsXFxdq/f79Onz6tNWvWKDo62h+jAABgHMvOvLOzszVhwgTl5ubK4XAoMzNTMTExioiIUMeOHTVy5Ei99NJLkqSuXbsqMjLSqlEAAAgoNq/X6/X3EBUR6JdGAh2XzXGt6jt+tb9HwBV4LznG3yNY6pq6bA4AAP484g0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhiHeAAAYhngDAGAY4g0AgGGINwAAhnFYefCxY8dq27ZtstlsGjZsmJo2berbNn/+fH366aey2+1q0qSJXnvtNStHAQAgYFzWmfeRI0dUVFRUoX03b96snJwcLV68WG63W26327etuLhYs2fP1vz587Vw4ULt3btX33777eVNDgDAdapC8d66datiY2P10EMPqVOnTurSpYu2b99+ydtkZWUpNjZWktSoUSMVFRWpuLhYklSlShVVqVJFpaWlOn36tI4fP65atWpd4V0BAOD6UKHL5lOmTNFbb72lxo0bS5K+//57ud1uzZ8/v9zbFBQUKCoqyrccFhYmj8ejmjVrqmrVqhowYIBiY2NVtWpVPfzww4qMjLzCuwIAwPWhQvG22+2+cEvSXXfdpaCgoMv6Ql6v1/fv4uJizZw5UytWrFDNmjXVp08f/fjjj7rjjjvKvX1o6A1yOC7va+La4nSG+HsEAAHmen1cqXC8V65cqdatW0uS1q1b94fxdrlcKigo8C3n5+fL6XRKkvbu3av69esrLCxMktS8eXNlZ2dfMt6FhaUVGRXXKKczRB7PMX+PASDABPrjSnm/nFToOe9Ro0Zp8eLFat++vTp06KClS5dq1KhRl7xNdHS0MjMzJUk7duyQy+VSzZo1JUnh4eHau3evTpw4IUnKzs7WrbfeWtH7AgDAda1CZ96lpaWaPXv2ZR24WbNmioqKUkJCgmw2m1JSUpSenq6QkBB17NhR/fr1U+/evRUUFKR7771XzZs3/1N3AACA643Ne/6T0eXo3bu3/vWvf1XGPOUK9EsjgY7L5rhW9R2/2t8j4Aq8lxzj7xEsVd5l8wqdederV0+9evXSPffcoypVqvjWDx48+OpMBwAAKqxC8Y6IiFBERITVswAAgAqoULz79++vb775xve89OrVq9WuXTsr5wIAAOWo0KvNU1JStHbtWt/y5s2beS9yAAD8pELx/vnnn/XSSy/5lpOTk7V//37LhgIAAOWrULxPnDihI0eO+Jbz8vL022+/WTYUAAAoX4We8x4wYIC6deumunXr6syZM8rPzy/zKWEAAKDyVCje7du317///W/t2bNHNptNDRs2VPXq1a2eDQAAXESF4j1t2rSLrufvvAEAqHwVes47KCjI97+zZ89q06ZNOnaMd8sCAMAfKnTm/fzz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Wrt2rY4ePVruvj/88IOGDBmimTNnatKkSUpKStLbb7+tDz/8UG3atNH27dv122+/6ezZs/r666/1wAMP+PPbAPjFqVOn9MUXX6hWrVpasWKFFi5cqPnz52vlypU6cOCA3n//fT300EOaN2+eTp48WaFjFhUVqU2bNpo3b56mTZumtLQ037bbbruNcF+jOPNGuX766Sf16tXLtxwZGanvv/9er732miTp1VdflXTuTPill16SJLVs2dL3Ea8NGjQo8656x44dU3Z2drn7hoaGKjg4WGFhYbrllltUUlKiY8eOKSgoSO3atdPatWvldDrVvHlzBQcHV843AfCz838Od+7cqaeffloul0s5OTnq3bu3JKmkpES5ubnau3evunbtKkmKiYnRd99994fHv/HGG/Xdd99p8eLFstvtOnLkiG9b06ZNLbhHuBqIN8p1see8H3nkkQvep95ms/nWnTp1Snb7uQs6v39BjdfrrdC+DseF/7fs3r27Zs2apfDwcHXr1u0K7xlgjvN/DgcNGqTIyEhJUrt27TR69Ogy+86cOVM2m02SfP/9vVOnTpVZ/uyzz1RUVKQFCxboyJEjiouL822rUqXKVbsfuLq4bI7L0qRJE23cuFGSNG3aNG3YsEF333237/m0LVu2XPAK9fNdzr7nu/POO5WXl6ft27fr/vvvv8J7AZjplVde0aRJkxQVFaVNmzbp+PHj8nq9GjNmjE6cOKEGDRooOztbkrRu3Trf7Ww2m44fP67jx4/rhx9+KHPMwsJCRUREyG63a9WqVRW+3A7/4swb5fr9ZXNJGjhwoN566y0tWLBAdevW1fPPP69GjRrptdde04cffqgqVapo7NixF/x2/z+DBg2q8L6/Fx0drZKSknLPKIBAV79+fXXu3FmLFi1S7969lZiYqKCgIMXGxqpatWrq3bu3kpKSlJmZqXvuucd3ZeuJJ55Qjx491KhRI0VFRZU5ZqdOndS/f399++23evzxx1WnTh3fa1Fw7eLtUWEEr9erv//97xo1apT+8pe/+Hsc4Jq0e/duHT16VPfdd58+++wzbdq0Sampqf4eCxbgzBvXvP3792vQoEHq0qUL4QYuoUaNGhoxYoRsNpvsdrvGjRvn75FgEc68AQAwDC9YAwDAMMQbAADDEG8AAAzDC9aA60B+fr7eeOMN7dq1SzVq1JB07s/+Dh48qA0bNmjSpEl+nhDA5SDeQIDzer0aMGCAunfv7ov0zp071bdvXyUlJfl5OgB/BvEGAlxWVpZsNluZT5K6/fbbtXz5cn3xxRe+datWrdK7776r4OBgnTlzRm+88YYiIiL0wQcf6NNPP1X16tVVrVo1TZw4USdPntTLL78sSTpx4oTi4+MVFxenAwcOaNSoUTp+/LhKS0v14osvqnXr1pV+n4FAR7yBALd7927dfffdF6yvVatWmeWjR49q6tSpqlevnmbOnKn58+dryJAhmj59ujIzM3XzzTfryy+/VH5+vrKystSwYUONGjVKv/32mxIRCaIAAAILSURBVD766CNJ0siRI9W3b1/99a9/lcfjUXx8vFauXHnR96sH8OfxEwUEuKCgIJ05c+YP97v55ps1ZMgQeb1eeTwe3XvvvZKkuLg4Pf300+rcubO6dOmiyMhIORwOLViwQMnJyWrbtq3i4+MlSZs2bVJJSYnv0+IcDocOHTqkW265xbo7CFyHiDcQ4Bo3buw7Mz7fzp07dfz4cUnnPmkqKSlJH3/8sW699VbNmzfP9wEXQ4cOVW5urtauXasBAwZoyJAhatu2rZYtW6YtW7ZoxYoV+uCDD7Ro0SIFBwcrLS1NYWFhlXofgesNfyoGBLgWLVqoRo0aeuedd3zrdu/erf79+/s+irWkpER2u13h4eH67bff9MUXX+jkyZMqKipSWlqa6tatqyeffFKJiYn67rvvlJGRoe+++06tW7dWSkqKfv31V50+fVr33XefPv/8c0nS4cOH5Xa7/XKfgUDHmTdwHXjnnXc0btw4devWTbVr11bVqlX1z3/+U3v27JEk1a5dW926dVNcXJzq1aunfv366dVXX9WGDRtUUlKiuLg43XjjjXI4HHK73Tp8+LBSUlIUHBwsr9erZ555Rg6HQ6+99ppGjBihZcuW6eTJk+rfv7+f7zkQmHhvcwAADMNlcwAADEO8AQAwDPEGAMAwxBsAAMMQbwAADEO8AQAwDPEGAMAwxBsAAMP8fz1KwMMieAabAAAAAElFTkSuQmCC\n",
            "text/plain": [
              "<Figure size 576x396 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IbO8CjekDdbk",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 170
        },
        "outputId": "0f917524-9158-48af-b8d2-a91dfa5d348b"
      },
      "source": [
        "df[\"Tempo_envio\"].describe()"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count                 904.00\n",
              "mean                    8.54\n",
              "std                     3.06\n",
              "min                     4.00\n",
              "25%                     6.00\n",
              "50%                     9.00\n",
              "75%                    11.00\n",
              "max                    20.00\n",
              "Name: Tempo_envio, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yVBuChl7D-LK",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 347
        },
        "outputId": "4a661f48-67f7-414e-9993-941548179c6d"
      },
      "source": [
        "#Gráfico de Boxplot\n",
        "plt.boxplot(df[\"Tempo_envio\"]);"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 576x396 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AAso8LU5GiFN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 347
        },
        "outputId": "69919c67-916c-490c-a647-1462e363612f"
      },
      "source": [
        "#Histograma\n",
        "plt.hist(df[\"Tempo_envio\"]);"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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AaAAggwABRBkACiAIANAAQQZAAogyABQAEEGgAIIMgAUQJABoACCDAAFEGQAKIAgA0ABBBkACiDIAFAAQQaAAggyABRAkAGgAIIMAAUQZAAogCADQAEEGQAKIMgAUABBBoACCDIAFECQAaAAggwABRBkACiAIANAAQQZAAogyABQAEEGgAIIMgAUoKbSA1Cery14stIjABxzPEMGgAIIMgAUQJABoACCDAAFEGQAKIAgA0ABBBkACiDIAFAAQQaAAggyABRAkAGgAIIMAAUQZAAogCADQAEEGQAKIMgAUABBBoACCDIAFECQAaAAggwABRBkACiAIANAAWq685c2bdqUmTNn5rTTTkuSfOITn8jXv/713HzzzTlw4EAaGxtz1113pba2tkeHBYBq1a0gJ8lnP/vZ3H///R1/njNnTpqbmzNx4sTcc889aW1tTXNzc48MCQDVrscuWW/atCljx45NkowePTobN27sqZsGgKrX7WfIL7zwQq6//vrs2rUrM2bMyL59+zouUQ8aNChtbW2d3saAAfWpqenb3RGAKtbY2HBEzi1dtexSLXskR2+XbgX5//7v/zJjxoxMnDgxL730Uq6++uocOHCg4+MHDx7s0u3s3Lm3O3cPHAPa2l7v0nmNjQ1dPrd01bJLteyR9Pwuh4t7ty5Zn3TSSbnooovSp0+fnHzyyRk8eHB27dqV/fv3J0m2b9+epqam7k0LAMegbgV5zZo1+cEPfpAkaWtryyuvvJLLLrssa9euTZKsW7cuo0aN6rkpAaDKdeuS9ZgxY3LTTTfliSeeyFtvvZXbb789p59+em655Za0tLRkyJAhmTRpUk/PCgBVq1tBPv7447N06dL3HF++fPkHHggAjkXeqQsACiDIAFAAQQaAAggyABRAkAGgAIIMAAUQZAAogCADQAEEGQAKIMgAUABBBoACCDIAFECQAaAAggwABRBkACiAIANAAQQZAAogyABQAEEGgAIIMgAUQJABoACCDAAFEGQAKIAgA0ABBBkACiDIAFAAQQaAAggyABRAkAGgAIIMAAUQZAAogCADQAEEGQAKIMgAUABBBoACCDIAFECQAaAAggwABRBkACiAIANAAQQZAAogyABQAEEGgAIIMgAUQJABoACCDAAFEGQAKIAgA0ABBBkACiDIAFAAQQaAAggyABRAkAGgAIIMAAUQZAAogCADQAFqevoG77zzzmzZsiV9+vTJ3Llz85nPfKan7wIAqk6PBvl3v/td/vrXv6alpSUvvvhi5s6dm5aWlp68CwCoSj0a5I0bN2bcuHFJklNPPTW7du3KP//5zxx//PE9eTcAVImvLXiy0iMc1i/+35eP2n316GvI7e3tGTBgQMefBw4cmLa2tp68CwCoSj3+GvI7HTx48LAfb2xs6NH7O5r/kwHK0dNfSyqpWnbp6h694ev20fo36dFnyE1NTWlvb+/4844dO9LY2NiTdwEAValHg/z5z38+a9euTZI8++yzaWpq8voxAHRBj16yHj58eD796U/nqquuSp8+fXLbbbf15M0DQNXqc7CzF3oBgCPOO3UBQAEEGQAKUFVB3r9/f8aNG5ef/OQnlR7lA1mzZk0uueSSXHbZZVm/fn2lx+mWPXv2ZMaMGZk2bVquuuqqbNiwodIjdctzzz2XcePGZeXKlUmSl19+OdOmTUtzc3NmzpyZN998s8ITds2h9rjmmmsyderUXHPNNb3q/QL+e5f/2LBhQz75yU9WaKru+e9d3nrrrcyaNStXXHFFvvrVr2bXrl0VnrDr/nuX3//+9/nKV76SadOm5brrrus1uyxatChTpkzJ5ZdfnnXr1h3Vx3xVBfn73/9+TjzxxEqP8YHs3LkzS5YsyapVq7J06dI88cQTlR6pW37605/mlFNOyYoVK3LffffljjvuqPRI79vevXszb968jBgxouPY/fffn+bm5qxatSpDhw5Na2trBSfsmkPtce+99+bKK6/MypUrc+GFF2b58uUVnLDrDrVLkrzxxht56KGHetWPWR5ql9WrV2fAgAFpbW3NRRddlD/84Q8VnLDrDrXL/Pnzc8cdd2TFihU5++yze8XbKD/11FN5/vnn09LSkocffjh33nnnUX3MV02QX3zxxbzwwgv5whe+UOlRPpCNGzdmxIgROf7449PU1JR58+ZVeqRuGTBgQF577bUkye7du9/1Dm69RW1tbZYtW5ampqaOY5s2bcrYsWOTJKNHj87GjRsrNV6XHWqP2267LePHj0/y7n+r0h1qlyRZunRpmpubU1tbW6HJ3r9D7fLrX/86l1xySZJkypQpHZ9rpTvULu/8vNq1a1ev+Bpw3nnn5b777kuSnHDCCdm3b99RfcxXTZAXLlyY2bNnV3qMD+xvf/tb9u/fn+uvvz7Nzc294gv+oXzpS1/K3//+91x44YWZOnVqbrnllkqP9L7V1NSkrq7uXcf27dvX8UV/0KBBveJS76H2qK+vT9++fXPgwIGsWrUqF198cYWme38Otctf/vKX/PGPf8zEiRMrNFX3HGqXbdu25Te/+U2mTZuWG2+8sdf8R+lQu8ydOzfTp0/P+PHj8/TTT+fSSy+t0HRd17dv39TX1ydJWltbc8EFFxzVx3xVBPlnP/tZzjrrrHz84x+v9Cg94rXXXssDDzyQBQsWZM6cOZ2+BWmJfv7zn2fIkCH51a9+lUcffTTf+973Kj1Sj+uN/y7vdODAgdx888353Oc+955LwL3J/PnzM2fOnEqP0SMOHjzY8VLPaaedlgcffLDSI3XbvHnz8sADD2Tt2rU555xzsmrVqkqP1GWPP/54Wltb893vfvddx4/0Y/6Ivpf10bJ+/fq89NJLWb9+ff7xj3+ktrY2H/3oRzNy5MhKj/a+DRo0KGeffXZqampy8skn57jjjsurr76aQYMGVXq092Xz5s05//zzkySf+tSnsmPHjhw4cCB9+/at8GQfTH19ffbv35+6urps3779PZdOe5M5c+Zk6NChmTFjRqVH6bbt27fnz3/+c2666aYk/3673qlTp77nG756i8GDB+e8885Lkpx//vlZvHhxhSfqvj/96U8555xzkiQjR47ML37xiwpP1DUbNmzI0qVL8/DDD6ehoeGoPuar4hnyvffemx//+MdZvXp1Jk+enG9+85u9MsbJvx+ETz31VP71r39l586d2bt3b6947eW/DR06NFu2bEny78twxx13XK+PcfLvLyz/eXvYdevWZdSoURWeqHvWrFmTfv365dvf/nalR/lATjrppDz++ONZvXp1Vq9enaampl4b4yS54IILOn4i4dlnn80pp5xS4Ym6b/DgwXnhhReSJFu3bs3QoUMrPFHnXn/99SxatCgPPvhg+vfvn+ToPuar7p26Fi9enI997GO57LLLKj1Kt/3oRz/q+E6+b3zjG73mGzveac+ePZk7d25eeeWVvP3225k5c2avuyz6zDPPZOHChdm2bVtqampy0kkn5e67787s2bPzxhtvZMiQIZk/f3769etX6VEP61B7vPLKK/nwhz/c8V7zp556am6//fbKDtoFh9pl8eLFHV88x4wZkyefLPv36/7H//r8uuOOO9LW1pb6+vosXLgwgwcPrvSonTrULjfeeGMWLVqUfv365cQTT8ydd96ZE044odKjHlZLS0sWL178rv8ILViwILfeeutRecxXXZABoDeqikvWANDbCTIAFECQAaAAggwABRBkACiAIANAAQQZAAogyABQgP8Pr6ZGkH5Vo7AAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 576x396 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hkxhLlATHMN3",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "c5e19e4f-d830-416f-ce78-7367926adb04"
      },
      "source": [
        "#Tempo mínimo de envio\n",
        "df[\"Tempo_envio\"].min()"
      ],
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qg1q3fAKIDtM",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "9f4667ac-1557-4591-9fdc-5436c14099c5"
      },
      "source": [
        "#Tempo máximo de envio\n",
        "df['Tempo_envio'].max()"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "20"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BiOyhekfIgLb",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        },
        "outputId": "732adad6-aa24-4067-a926-7aacf59992e0"
      },
      "source": [
        "#Identificando o Outlier\n",
        "df[df[\"Tempo_envio\"] == 20]"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data Venda</th>\n",
              "      <th>Data Envio</th>\n",
              "      <th>ID Loja</th>\n",
              "      <th>ID Produto</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>No. Venda</th>\n",
              "      <th>Custo Unitário</th>\n",
              "      <th>Preço Unitário</th>\n",
              "      <th>Quantidade</th>\n",
              "      <th>Valor Desconto</th>\n",
              "      <th>Valor Venda</th>\n",
              "      <th>Produto</th>\n",
              "      <th>Fabricante</th>\n",
              "      <th>Marca</th>\n",
              "      <th>Classe</th>\n",
              "      <th>Cor</th>\n",
              "      <th>custo</th>\n",
              "      <th>lucro</th>\n",
              "      <th>Tempo_envio</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2008-05-09</td>\n",
              "      <td>2008-05-29</td>\n",
              "      <td>199</td>\n",
              "      <td>384</td>\n",
              "      <td>18839</td>\n",
              "      <td>200805093CS607</td>\n",
              "      <td>348.58</td>\n",
              "      <td>758.00</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4,548.00</td>\n",
              "      <td>Adventure Works Laptop15.4W M1548 Red</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Adventure Works</td>\n",
              "      <td>Regular</td>\n",
              "      <td>Red</td>\n",
              "      <td>2,091.48</td>\n",
              "      <td>2,456.52</td>\n",
              "      <td>20</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Data Venda Data Envio  ...                lucro  Tempo_envio\n",
              "0 2008-05-09 2008-05-29  ...             2,456.52           20\n",
              "\n",
              "[1 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xL5IKMeeLI6v",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "df.to_csv(\"df_vendas_novo.csv\", index=False)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NLtTuecu62_h",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}