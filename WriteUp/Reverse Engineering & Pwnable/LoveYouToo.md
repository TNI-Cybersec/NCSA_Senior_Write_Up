# LoveYouToo.exe

## Step 1 : Improvise 
### Uses [dnSpy](https://github.com/dnSpy/dnSpy) for inspecting code


## Step 2 : Adapt
### Duplicating `Crypto` Class
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

  private static byte[] _salt = Encoding.ASCII.GetBytes("23f4da7ad7ac9a74be5f5b245efde5fc");
}
``` 

## Step 3 : Overcome
### Reversing
```cs
  static void Main(string[] args)
  {
    string value = Crypto.DecryptStringAES("EAAAAGz7DpD5aG6v2wq24/WsA6/rFAV7KsPco0oDUgnNRE2UHownh8ClTUCMIxWg+HECKQ==");
    Console.WriteLine("Password = " + value);
    Console.WriteLine("Success! Flag: " + Crypto.DecryptStringAES("EAAAAGa6e4r58bf05YW/yPHVuV6dUGOn9KjQVegAQtiU57mNMamgWS4F/5VmRc4RftmdLdOCWfmXLSxdLbaFLv9BJgk=") + "!");
    Console.ReadLine();
  }
```
### Result
```bash
Password = i love littledog
Success! Flag: NCSA{4933062932cb4ec35c0818af29a15b1d}!
```

![Imgur](https://i.imgur.com/77otpco.jpeg)
