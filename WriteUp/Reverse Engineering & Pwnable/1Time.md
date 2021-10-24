# 1Time.exe

วันนี้เรามาลองแก้ปัญหาข้อนี้ด้วย IAO Methodology กันนะครับ ;w;

uses same ๆ step from [next](LoveYouToo.md) solution 💔

## Step 1 : Improvise 
### Uses [dnSpy](https://github.com/dnSpy/dnSpy) for inspecting code
1. drags and drops `1Time.exe` in **dnSpy**
2. found sth interesting as photos below; `Program` and `Crypto` Class

![Imgur](https://imgur.com/jVl9ite.png)
![Imgur](https://imgur.com/OUdBqVe.png)

> PS: actually, you can try reversing the `Program.main` here..., but i'm too lazy lol

## Step 2 : Adapt
### Duplicates `Crypto` Class from dnSpy
> using Visual Studio for C# project
```cs
public class Crypto
{
  public static string EncryptStringAES(string plainText, string sharedSecret)
  {
    if (string.IsNullOrEmpty(plainText))
    {
      throw new ArgumentNullException("plainText");
    }
    if (string.IsNullOrEmpty(sharedSecret))
    {
      throw new ArgumentNullException("sharedSecret");
    }
    string result = null;
    RijndaelManaged rijndaelManaged = null;
    try
    {
      Rfc2898DeriveBytes rfc2898DeriveBytes = new Rfc2898DeriveBytes(sharedSecret, Crypto._salt);
      rijndaelManaged = new RijndaelManaged();
      rijndaelManaged.Key = rfc2898DeriveBytes.GetBytes(rijndaelManaged.KeySize / 8);
      ICryptoTransform transform = rijndaelManaged.CreateEncryptor(rijndaelManaged.Key, rijndaelManaged.IV);
      using (MemoryStream memoryStream = new MemoryStream())
      {
        memoryStream.Write(BitConverter.GetBytes(rijndaelManaged.IV.Length), 0, 4);
        memoryStream.Write(rijndaelManaged.IV, 0, rijndaelManaged.IV.Length);
        using (CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write))
        {
          using (StreamWriter streamWriter = new StreamWriter(cryptoStream))
          {
            streamWriter.Write(plainText);
          }
        }
        result = Convert.ToBase64String(memoryStream.ToArray());
      }
    }
    finally
    {
      if (rijndaelManaged != null)
      {
        rijndaelManaged.Clear();
      }
    }
    return result;
  }

  public static string DecryptStringAES(string cipherText)
  {
    if (string.IsNullOrEmpty(cipherText))
    {
      throw new ArgumentNullException("cipherText");
    }
    RijndaelManaged rijndaelManaged = null;
    string result = null;
    try
    {
      Rfc2898DeriveBytes rfc2898DeriveBytes = new Rfc2898DeriveBytes("4c 69 54 74 31 65 44 40 67", Crypto._salt);
      using (MemoryStream memoryStream = new MemoryStream(Convert.FromBase64String(cipherText)))
      {
        rijndaelManaged = new RijndaelManaged();
        rijndaelManaged.Key = rfc2898DeriveBytes.GetBytes(rijndaelManaged.KeySize / 8);
        rijndaelManaged.IV = Crypto.ReadByteArray(memoryStream);
        ICryptoTransform transform = rijndaelManaged.CreateDecryptor(rijndaelManaged.Key, rijndaelManaged.IV);
        using (CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Read))
        {
          using (StreamReader streamReader = new StreamReader(cryptoStream))
          {
            result = streamReader.ReadToEnd();
          }
        }
      }
    }
    finally
    {
      if (rijndaelManaged != null)
      {
        rijndaelManaged.Clear();
      }
    }
    return result;
  }

  private static byte[] ReadByteArray(Stream s)
  {
    byte[] array = new byte[4];
    if (s.Read(array, 0, array.Length) != array.Length)
    {
      throw new SystemException("Stream did not contain properly formatted byte array");
    }
    byte[] array2 = new byte[BitConverter.ToInt32(array, 0)];
    if (s.Read(array2, 0, array2.Length) != array2.Length)
    {
      throw new SystemException("Did not read byte array properly");
    }
    return array2;
  }

  private static byte[] _salt = Encoding.ASCII.GetBytes("28a408b8cdc386749bfb345975fb76bb");
}
``` 

## Step 3 : Overcome
### Reversing
```cs
  static void Main(string[] args)
  {
    Console.WriteLine("Success! Flag: " + Crypto.DecryptStringAES("EAAAAJA/nSl4G+Bk/dKAHebLp8xicPH2HRuZthGOXVe5P46HEYd3h2f8MTXHUy4jkrCsDp6PRPK0+mah3E1Z7VPtMQc=") + "!");
    Console.ReadLine();
  }
```
### Result
```cmd
Success! Flag: NCSA{c29b8ad5076fde6b56ea1519a5c2145f}}!
```

![Imgur](https://i.imgur.com/77otpco.jpeg)
