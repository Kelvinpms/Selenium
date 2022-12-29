using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading;

IWebDriver navegador = new ChromeDriver();
navegador.Url = "https://consultacnpj.com/cnpj/";
navegador.Manage().Window.Maximize();
Thread.Sleep(2000);
string[] cnpjs = { "45997418000153", "72273196001090", "33000167000101" };

foreach (string cnpj in cnpjs)
{
    IWebElement input = navegador.FindElement(By.XPath, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/input');
    input.Clear();
    input.SendKeys(cnpj);
    Thread.Sleep(1000);
    IWebElement texto = navegador.FindElement(By.XPath, '//*[@id="company-data"]');
    System.IO.File.WriteAllText(cnpj + ".csv", texto.Text, System.Text.Encoding.UTF8);
    Thread.Sleep(2000);
}

navegador.Quit();
