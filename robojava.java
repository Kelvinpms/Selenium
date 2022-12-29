import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

WebDriver navegador = new ChromeDriver();
navegador.get("https://consultacnpj.com/cnpj/");
navegador.manage().window().maximize();
navegador.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
String[] cnpjs = { "45997418000153", "72273196001090", "33000167000101" };

for (String cnpj : cnpjs) {
    WebElement input = navegador.findElement(By.xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/input'));
    input.clear();
    input.sendKeys(cnpj);
    navegador.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
    WebElement texto = navegador.findElement(By.xpath('//*[@id="company-data"]'));
    BufferedWriter writer = new BufferedWriter(new FileWriter(cnpj + ".csv"));
    writer.write(texto.getText());
    writer.close();
navegador.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
}

navegador.quit();

