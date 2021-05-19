# RW Research
![](https://cdn-images-1.medium.com/fit/t/1600/480/1*zSPtMkp70YN9JDhFRaHHXA.jpeg)
Purely educational research

## Notes
  1. This is only meant to be used for a very specific case study
  2. Everything here assumes that this entire repository has been downloaded via a backdoor
  3. This repository should be placed in the directory that contains the files that are to be encrypted or decrypted
  4. At the moment, only `index.php` and `*.txt` files are handled
  5. The key for decryption is saved on the victim's machine once `key_generator.py` is run. DO NOT DELETE once it is generated. Keep it stored on the victim's machine (remember, this isn't the real thing, demo only), or copy it to another machine for future decryption

## Instructions
  1. Generate a key to lock the file/s you want locked running the following: `python RWResearch/attacker/key_generator.py`
  2. Select a file you want encrypted using: `python RWResearch/encrypt_decrypt.py -e key.key file_to_be_encrypted`
  3. To decrypt, use `python RWResearch/encrypt_decrypt.py -d key.key file_to_be_decrypted`

## Ideas to try/improve on
  ### Attacker
  * Encrypt any kind of file, while being able to recover the correct file type when decrypting
  * Instead of defacing the site, create a duplicate that uploads the ransomware to legitimate customers
  * A better idea of using the key on the victim machine that ensures it's only used by the attacker
  * Add some `this looks like a legit hacking tool` terminal art when running the tool (maybe progress bar, etc) for the lolz
  ### Defender
  * Use ELK/EFK/ stack (or Splunk) to set up monitoring
    * Can it pick up priv esc attempts
    * Nmap scans?
    * failed ssh tries
  * Get all monitoring systems dumping P1s and P2s to a Slack channel via webhooks?
