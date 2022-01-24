# B3Project-Ingestion
<html>

<div class="introduction">
<p>
O Projeto B3 consiste em um projeto de extração e armazenamento de dados históricos de ações da B3, a ideia princiapal é centralizar os dados de diferentes ações em um único. Existe algumas formas mais simples de se fazer isso utilizando, como utilizando a biblioteca pandas_datareader e a yfinance, mas o intuito aqui é fazer a ingestão de uma forma alternativa usando Python e Selenium para baixar o arquivo diretamente da página web.
</p>
</div>

<br>
<div class="tech">
<h2>Tecnologias</h2><br>


<table>
<tr>
    <td width="30%">
        <img src="https://github.com/povoaaires/B3Project/blob/main/assets/ADF.png" style="width=125; height:75px;">
    </td>
    <td style="width:100">Utilizado para fazer a orquestração de dados do projeto, o ADF irá movimentar dados entre as camadas do Data Lake.
    </td>


</tr>

<tr>
<td width="30%">
        <img src="https://github.com/povoaaires/B3Project/blob/main/assets/ADLS.png"style="width=125; height:75px;">
    </td>
    <td style="width:100">Separado em três camadas, bronze, silver e gold, sendo que a primeira camada recebe o dado cru, a intermediária faz a agregação de todos os dados em um único arquivo e a camada gold é a de disponibilização para o cliente final consumir
    </td>


</tr>

<tr>
<td width="30%">
        <img src="https://github.com/povoaaires/B3Project/blob/main/assets/logicapp.png"style="width=125; height:75px;">
    </td>
    <td style="width:100">É responsável por acessar todos os arquivos JSON na pasta do OneDrive e jogá-las na primeira camada do Data Lake
    </td>


</tr>

</table>

</div>

<br><br>
<div class="flow">
<h2>Arquitetura</h2><br>

<img src="https://github.com/povoaaires/B3Project/blob/main/assets/B3Project-Architecture-v1.png">

</div>

</html>