---
PGP CONTINUED
---
3985


<p>Ok, so by now I am assuming you have Tails running. Let&#8217;s learn how to use PGP within Tails. First thing you are going to want to do is create your own personal key, which consists of your public key that you can give out to people or post in your profiles online. As mentioned before, this is the key people use to encrypt messages to send to you. Your personal key also consists of your private key which you can use to decrypt messages that are encrypted using your PGP public key.</p>
<p>If you look up to the top right area, you will see a list of icons, and one o them looks like a clipboard. You need to click on that clipboard and click <strong>Manage Keys</strong></p>
<p>Next click <strong>File</strong> -&gt; New<br />
Select PGP Key and click Continue<br />
Fill out your full name (I suggest you use your online name, not your real name)<br />
Optionally fill out an email and a comment as well.<br />
Next, click Advanced Key Options.<br />
Make sure Encryption type is set to RSA and set key strength to 4096.<br />
Once you have done this, click Create and it will generate your key.</p>
<p>Once you have done this, you can view your personal key by clicking the tab <strong>My Personal Keys</strong>. You have now created your personal key! To find your PGP public key, you right click on your personal key and click Copy and it will copy your PGP public key to your clipboard, in which you can paste anywhere you wish. A PGP public key will look something like this.</p>
<p>&#8212;&#8211;BEGIN PGP PUBLIC KEY BLOCK&#8212;&#8211;</p>
<p>mQINBFLLWDcBEADEzn3mnLsezUDDAS5Q0lm1f6JdkI534WPuRlAN8pnuQsCSwUQU<br />
hPEAgNCUNhxN4yCJ1mDt9xpXpX8QzsMIcofCHeE9TMLAnHzbmXLLi+D8sPZpLpDN<br />
6jEIFvmBD4dvp5adimvRl8Ce49RpO345VUz8Ac0qLSmsv2u+kQviDQXZkrrxXHnA<br />
IalvgDopXTISa9Sh7J3HHYYQazOZt9mfAjjuuRdaOqmAAtEe9dl43nrx+nSd/fqH<br />
13XvMKhqJhIoJ02CBFfRBm86vtx5yiXqHZX438M9kbASqU0A2jAfRd+IZG5Z9gCI<br />
W6FTror+F4i+bEdAuGTG1XFsQSgjKTIG0vgYiTJ93C2MZxrLvNnJp0g2zD0URyk8<br />
Y2IdyCDfIL10W9gNMqLmjD0z/f/os66wTJkflSGaU9ZsrKHUKFN5OSfOZtNqktWn<br />
fCpY4bigkJ8U/5C8mtr9ZE3Tv+RV4rPY0hAOtZucnhlRmYKVFNjvbS0MjqA1188c<br />
wzBNG0XcpCNtmM5UsSvXwnDoUaEMXe50Hikxdk3d+CJzqYnor72g/WmIDROCiXl6<br />
2D9rJ2JuLpl9bQLM+KCbXJf3kUSvzszZGXL/AwmynvqlruaXqr5975sCdfqXVexx<br />
1sxsLofOzE01xSDEJRWwHQPlxTKPZFnXD709Xumjdinjv1w4onLk04Z96wARAQAB<br />
tC5Kb2xseSBSb2dlciAoVGhleSB3b3VsZCBsaXZlIGFuZCBkaWUgdW5kZXIgaXQp<br />
iQI3BBMBCgAhBQJSy1g3AhsDBQsJCAcDBRUKCQgLBRYCAwEAAh4BAheAAAoJEPuh<br />
6tSg81nyzNsP/2ayrAz4InCK/ZnyRnnsjSHIXMv7t2uDTbYomA/0B6v/S6wHMNZX<br />
G6+sYg41mfMuZEimgavNb0Uc2r6mI7UyWy5lp1Gd/D+all81X7bm5EBpvl1isPgJ<br />
EqjehEdh9FQjrTiRIJafM1m254hIAaZ1RvAphI0tM2lpudk+tNKq+ivV8PpsN9TP<br />
0mg5ZAu1lIKtG9k5vS9HAQ0grJ01TFMEjlifrf7eRyJ1+dmRJ+Xtoy2js8UwS+wM<br />
RrIi3G39P2BfEZFQka3EmQ2JgN4pDWFoI0hODGhTba8Z0XSnVtabOTi1TOWIFmFu<br />
yqA9bNtuOt3KhIC/O+mEATRsc/VPbTY+80kf45LwlDBfKO3PcOXSOG7ygibzEqXn<br />
Ms/Rfe1kNEBeR9Wx2NMJSdxypqGij17CLJwNLC3KypTIQrhzy3YAndeDG4TadW2P<br />
v/FJxhz+MX+s+9VeX2fGC0Fsfp8JbeWMAznp8Rf6O/tzEYW+pbLoLRPdi/DvFBZV<br />
yWGPspzt3Qspm+BHbeW9iFjvCyvP2/DrKmQM7ABuRh/TMZR7uQ5na11L8rf3nzrS<br />
Al/lSul42xLzxG+h9mDixXd1Vh6rVGMbCjL7wO25TUneFo13U5J+klo1blQWV/DL<br />
FZUwhh2utWNCMCtcdRW0HYa14Wdyy7H68WmsJqBWUsbyD9PZ2gSawBy7uQINBFLL<br />
WDcBEACg3IOme+sg0OZN349UYRr9/O6uW2vC5x9/azZrFNSNYh/LFJTt3XI/FsjN<br />
gCj6NxRxbfdyLjL1gxSlJyFtclkFGS0lC0GIz7lINvemkewjde/bHXChz2IIaIli<br />
L2A6Z6w3fP4jlQCw8NoGGJ360WMkZVTDDakYYkb50BrZSx4TVLjrHfFuLMXTE255<br />
gQrId02jYO6240EDIhHITuiSwUQvHtXlOrHSohN83TD1I4H7iH/FLae9gYh4C/Ix<br />
VLkzLUqvpf72Q/xogCZAJl4WEMmWD6dXufvyvhCXQnbjiLuAdQas0ef/t652LPw/<br />
vJFDSDmguw9PXWpv3vFOe13UNU//+nw3kIGxaVWGvazXk8IFiDv9USgEGjcNn4zo<br />
8HQlQrYz9/gyI3XojGV6L8iecWpHSweqR3NxKJmWKWEG1wwnWPL8M+z6OwEvRdxV<br />
spy+eG0Zs+6igbw3tk6gJ4cq5ehdlmD6py27AhRhlj7uLlZxmK3uFV19QjtX/Dyt<br />
73ZNX16krXqufl0HAJRd1PwhITPCtSviW3L2qKF2Pdak3j97A656EcInCcAyOUC/<br />
mUNUDtXJik6uwFgFFn9/pnFr+acY7ppsWPG5rr7jRj+Lgjnjkckpkjo8jN1hZE17<br />
CfJyrYrSqdglCcIgTHteIEZdPfPUmnbbSoyeufkyEW1AoIKatQARAQABiQIfBBgB<br />
CgAJBQJSy1g3AhsMAAoJEPuh6tSg81ny4nIP/2lVf0DTp1n5xPEBZEUlgzcMNeh5<br />
FTIS3J44g5a+OlkRVgHFtu7K/MUsftlUzkvMMa0sXllhKc6syxcytoD7LAt9tbQh<br />
62yEzijTliU2QFgWJSS6IfbtC2IyRouAns3KD6XouKTFUs/i0n/QpwhnM+Ya/SAg<br />
c/oroM7SE/T4g+v6EeRCq7In/TMgc74j+25zUF1rVSCenbZKkYezxqZ33cXLwl7l<br />
IUBcK2uNHDBUB5G853NR0OkBm5i+KC8vM3K1/MZ+P/lK0xOcTGXZH/A7GrEsI4FJ<br />
nw5i6zJZb8gmDt44Tp/1Ujxnm5xhVWgnOQeSVSyiRsHQ/gTCL1PqsZhW7yulwL05<br />
yxZgN+oYVx4pNtLJMigRjoCY9IKEmZhY75cWXXA19j14Wnxu8IrwwSk1WyzMQcjj<br />
7onP4OEhbPuotqWqVAc0M/+MV5oMGIG0Qepy6XpZOCCpZw/p1rDrZSYP5eQMd/4x<br />
LB7xch6GjbWsnKhA1wGdjdclBodixorVfCRn4s5jTgXx7wWz/opM4ix/CPAkify7<br />
4Sf0BdJ5YtFILZc5StED4WC5pljJbdEWVsb9rn6egvFn7W/ZlDJAerS6Mt5LJGAh<br />
Aude0Kz2HJwDtOBF4nXeTzRCK5BrBnCYPHAtO2aqfowirzjMTd9A/ADoPmIbIJAm<br />
04mA6krRiH909Bnx<br />
=Az2N<br />
&#8212;&#8211;END PGP PUBLIC KEY BLOCK&#8212;&#8211;</p>
<p>Next, you are going to want to save the private key on a secondary USB drive or SD card. If you are running Tails from a USB drive, then you must use a separate drive to store your key on. If you are running Virtual Box, you want to <strong>right click</strong> on the icon in the bottom right corner that looks like a USB drive, and select your separate drive that you will be using to store your keys on. Again, never store your private keys on your hard drive, keep them OFF your computer.</p>
<p>To save your private key, you are going to right click on your personal key and click Properties. I know you probably saw where it says Export, but this is not what you want to do. Clicking export will ONLY export your public key and will not save your private key. If you lose your private key, you can never recover it even if you create another personal key using the exact same password. Each private key is unique to the time it was created and if lost, is lost forever. So once you have clicked <strong>Properties</strong>, go over to the tab <strong>Details</strong> and click <strong>Export Complete Key</strong>.</p>
<p>Once you have done this, you have saved your personal key for future use once you restart Tails. Remembering that Tails is not installed on your hard drive, so every time you restart Tails you lose all your keys. By saving your keys onto a USB drive or SD card, you can import your keys for use every time you restart it.</p>
<p>Next you are going to want to learn how to encrypt and decrypt messages using your key. Well, luckily for me, Tails has already made a tutorial on how to do this, so I will refer you to their webpage. But before I do that, I need to mention that you need to find somebody else&#8217;s PGP public key, or you can practice by using your own. Needless to say, the way you import other people&#8217;s keys into what&#8217;s called your <strong>key ring</strong> is by loading them into a text file. You do this with the program called <strong>gedit Text Editor</strong>.</p>
<p>Click Applications -&gt; Accessories -&gt; gedit Text Editor and enter in someone&#8217;s public key and hit save. Next you can return to your key program from the clipboard icon and click File -&gt; Import and select that file. It will import that person&#8217;s public key into your key ring. To add future public keys to your key ring, I suggest reopening the same file and just adding the next key below the previous key and each time you open that file it will load all keys within that file. This way you can keep all the PGP public keys together in one file and save it on your SD card or USB drive for future use.</p>
<p>Finally you can use the following 2 pages to learn how to encrypt and decrypt messages using PGP.</p>
<p>https://tails.boum.org/doc/encryption_and_privacy/gpgapplet/public-key_cryptography/index.en.html</p>
<p>https://tails.boum.org/doc/encryption_and_privacy/gpgapplet/decrypt_verify/index.en.html</p>
<p>Until next time. Have fun with your new found ability to communicate in PGP!</p>

Updated: 2014-02-12

