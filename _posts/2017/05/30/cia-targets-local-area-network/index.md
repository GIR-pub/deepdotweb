---
What CIA does on target&#8217;s Local Area Network"
---
<article class="post-listing post-20225 post type-post status-publish format-standard has-post-thumbnail hentry  tag-area tag-cia tag-local tag-network tag-targets">
    <div class="post-inner">
        <span>Posted by: <a href="https://www.deepdotweb.com/author/filipjelic/" title="">Filip Jelic </a></span>
    <span>May 30, 2017</span>
    
    <span><a href="https://www.deepdotweb.com/2017/05/30/cia-targets-local-area-network/#comments">3 Comments</a></span>
    </p>
    <div class="clear"></div>
    
    <p>Based on Wikileaks Vault 7 leak of CIA tools and documents, we can imagine what a data exfiltration attack to a corporate network by CIA looks like. I&#8217;m going to focus on the Local Network activity so let&#8217;s say there is already a compromised computer in the LAN that will be used as a pivot to further exploit the target organization. That part could&#8217;ve been done by some employee visiting CIA&#8217;s exploitation server that utilizes browser 0days or by opening a maliciously crafted document exploiting reader vulnerabilities. Even if that fails, agent could hack the router (RCE <a href="https://artkond.com/2017/04/10/cisco-catalyst-remote-code-execution/">Proof-Of-Concept</a> for over 300 Cisco models, based on Vault 7 leak) or attack the WiFi to get himself an entry into the LAN.</p>
    <p><strong>The arsenal</strong></p>
    <p>The arsenal is made of many building blocks to allow agents to create the perfect tool for the job, without unnecessary parts. When computer is first compromised, only core backdoor functionality is planted. Only when certain action is required, it is received to process memory just in time, executed and forgotten. This way, malicious code never touches the disk and doesn&#8217;t persist on target&#8217;s machine which helps a lot with antivirus and makes it very difficult to reverse engineer the program. I will first describe the main building blocks our fictional attack will rely on. These tools would vary based on target operating system, but the applied principles would be the same.</p>
    <p><strong>AfterMidnight</strong></p>
    <p>That Core backdoor thingy that waits for payload is dubbed <a href="https://wikileaks.com/vault7/document/AfterMidnight_v1_0_Users_Guide/AfterMidnight_v1_0_Users_Guide.pdf">AfterMidnight</a> and those payloads are called Gremlins. Let&#8217;s say that controlled machine in target LAN has AfterMidnight.dll and AfterMidnight Core on disk. Follow the diagram below as you read about this tool.</p>
    <p>DLL is in plain text and looks as innocent as possible. It persists as Windows Service DLL running from inside the netsvcs svchost.exe process. This stager finds AfterMidnight Core on disk and loads it into memory.</p>
    <p>Core handles the encrypted networking part and behaves strongly on the customized configuration which defines where and how often to report to Command &amp; Control server (Octopus). That server can be hosted as a real WAN server or even as another Gremlin on another machine.</p>
    <p>First thing Core expects is the Master Gremlin which is actually procedure plan with the encryption key. Note that encryption key never touches the disk and in most cases (including our case), neither does the Master Gremlin.</p>
    <p>When the predefined time comes, Master first downloads any needed Gremlins and stores them on the disk encrypted with the mentioned key. Now everything is ready and plan begins. Gremlins are loaded into memory as-needed according to the plan. It is impossible to retroactively find out what action was carried out because the encryption is so carefully carried out and everything is deleted after it&#8217;s no longer required, just in case.</p>
    <p>Following diagram shows it clearly:</p>
    <p><img class="wp-image-20231 aligncenter" src="/imgs/2017/05/word-image-114.png" srcset="/imgs/2017/05/word-image-114.png 469w, /imgs/2017/05/word-image-114-300x251.png 300w" sizes="(max-width: 469px) 100vw, 469px" /></p>
    <p>AfterMidnight is the program that is controlling the pivot and the program to be installed on target machine in this fictional mission. We owned 1 computer with it and we can load another weapon as a Gremlin compromise the target.</p>
    <p><strong>Archimede</strong></p>
    <p><a href="https://wikileaks.com/vault7/document/Archimedes-1_0-User_Guide/Archimedes-1_0-User_Guide.pdf">Archimede</a>, new version of <a href="https://wikileaks.com/vault7/document/Fulcrum-User_Manual-v0_62/Fulcrum-User_Manual-v0_62.pdf">Fulcrum</a>, is a tool which facilitates a controlled machine to pivot through LAN. The application will monitor the target machine’s HTTP traffic and redirect the target to the provided URL when the proper conditions are met. This is not an exploit or payload, but a simply a <a href="https://www.deepdotweb.com/2016/10/10/man-in-the-middle-attacks/">Man in the Middle</a> tool which makes sure that the victim in the same LAN reaches the URL of attacker&#8217;s choice. The setup of these tools is the same, but Archimede support iframe injection which might be useful if shorter paths are blocked.</p>
    <p><strong>Grasshopper</strong></p>
    <p>The framework for creating highly customized payloads for Windows machines &#8211; <a href="https://wikileaks.com/vault7/document/Grasshopper-v2_0_2-UserGuide/Grasshopper-v2_0_2-UserGuide.pdf">Grasshopper</a>. This tool provides the ability to create the perfect Master Gremlin and Gremlins based on the information gathered. Grasshopper allegedly shines when it comes to adjusting to the personal security products which Windows users tend to have installed.</p>
    <p>Both AfterMidnight and Grasshopper use Python 3.4 interpreter and everything seems compatible with each other. I really like the concept of building specialized weapons that come and go, without footprint.</p>
    <p>Now you&#8217;re introduced to our payload (AfterMidnight) pretty well and the attack vector tool (Archimede) and the rest will be described as we go.</p>
    <p><strong>Fun starts here</strong></p>
    <p>We have the pivot machine and I&#8217;m thinking about loading Archimede as a Gremlin to start a Man in the Middle attack. Archimede manual clearly allows creating DLL payload with predefined parameters which can be used as a Gremlin. Let&#8217;s prepare it (here it says Fulcrum, but it&#8217;s probably the same in Archimede).</p>
    <p>So you are just itching to use Fulcrum against this target of yours and you’re ready to dive in! Hang on there partner. First we need to gather the following information before we can build a deployment package:</p>
    <p>1. The MAC address of the LAN­side interface of the gateway</p>
    <p>2. The MAC address of the target machine</p>
    <p>3. The URL to inject into the HTTP response</p>
    <p>4. The Injection method of the HTTP response</p>
    <p>5. The character set of the pivot machine</p>
    <p>6. Any user agent string whitelist entries</p>
    <p>7. Any user agent string blacklist entries</p>
    <p>8. Any target content type modifications</p>
    <p>9. Whether the pivot machine is a laptop or a desktop</p>
    <p>10. The OS version of the pivot machine</p>
    <p>11. The bitness of the process Fulcrum will run in</p>
    <p>12. The privilege level of the process Fulcrum will run in</p>
    <p>13. What PSPs are present on the pivot machine</p>
    <p>14. How the Fulcrum files will be delivered to the pivot machine</p>
    <p>15. Where the Fulcrum files will be deployed to on the pivot machine’s file system</p>
    <p>16. When Fulcrum should be delivered to the pivot machine</p>
    <p>17. How Fulcrum will be started on the pivot machine</p>
    <p>18. When Fulcrum should be started</p>
    <p>19. If Fulcrum should be automatically restarted</p>
    <p>20. When Fulcrum should be shut down</p>
    <p>21. When Fulcrum should be removed</p>
    <p>Technical options first: we can use Grasshopper to get a DLL (Gremlin) that finds out technical information. Furthermore, let&#8217;s use so called Alpha Gremlin – custom scripting engine that we can use to programmatically find out gateway and target MAC, OS version, bitness, character set and present PSPs. Now we can run basic sniffer and MitM.</p>
    <p>We will start immediately, run MitM to gather information about victim&#8217;s browser and OS based on their internet traffic. Timing options will be set according to Archimede&#8217;s has &#8220;Fire and Forget&#8221; recommendation &#8211; everything except the core will be removed once the mission is done (on pivot). Other options are not needed for the first MitM.</p>
    <p>Grasshopper will make sure that we don&#8217;t upset pivot&#8217;s PSP, which is nice. Other options are not used yet as we need to gather more information, which we will with the basic sniffer and MitM functionality.</p>
    <p>This is the point where most of these attacks go other directions, let&#8217;s analyze the best and the worst scenario.</p>
    <p>Best case scenario, agent has a 0day for some technology used by the target, e.g. person uses vulnerable browser or OS. Agent would configure Archimede to redirect the first HTTP GET request to a server in LAN which is another Gremlin on the pivot. That Gremlin would simply deliver the AfterMidnight Core payload using that exploit.</p>
    <p>Worst case scenario, the target is not using any exploitable technology. Also, he configured the browser to block all HTTP traffic.</p>
    <p>Global adversaries such as CIA certainly have many legit TLS/SSL certificates which would be used here to make a realistic HTTPS server which will offer AfterMidnight to our victim. We need to exploit the human now, so these methods depend on user interaction. If one social engineering attack fails, we can just try another trick until we succeed.</p>
    <p>We would configure new Archimede Gremlin to perform MitM and another Gremlin to serve as HTTPS server. Once Archimede finds &#8216;download&#8217; in requested URL, it would redirect the target to our Gremlin server that hosts a copy of the requested website with all downloads available, but tampered with AfterMidnight installer. The target will become a victim once they open the downloaded executable. I assume most people don&#8217;t check the integrity checksums when downloading over SSL.</p>
    <p>Now we destroy everything except AfterMidnight Core on the first pivot and repeat the information gathering with Alpha Gremlin on the new machine. According to the previous step, we load Gremlins for that system and personal security product which will transfer interesting files to the <a href="https://wikileaks.org/ciav7p1/cms/files/UsersGuide.pdf">Hive</a>. If needed, we can load Gremlins for recording keyboard, microphone, webcam, screen activity etc.</p>
    <p>If you enjoyed reading this, I highly recommend diving into <a href="https://wikileaks.com/vault7/">Vault 7</a>, it will keep you entertained for hours. Perhaps take a look at more persistent, kernel level payloads such as those found in Dark Matter section.</p>
    </div>
    <a href="https://www.deepdotweb.com/tag/area/" rel="tag">area</a> <a href="https://www.deepdotweb.com/tag/cia/" rel="tag">cia</a> <a href="https://www.deepdotweb.com/tag/local/" rel="tag">local</a> <a href="https://www.deepdotweb.com/tag/network/" rel="tag">network</a> <a href="https://www.deepdotweb.com/tag/targets/" rel="tag">targets</a></span> <span style="display:none" class="updated">2017-05-30</span>
    <div style="display:none" class="vcard author" itemprop="author" itemscope itemtype="http://schema.org/Person"><strong class="fn" itemprop="name"><a href="https://www.deepdotweb.com/author/filipjelic/" title="Posts by Filip Jelic" rel="author">Filip Jelic</a></strong></div>
    
