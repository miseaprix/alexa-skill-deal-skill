# Skill Alexa Readable skill name for the Alexa skill

## Description

![Readable skill name for the Alexa skill Alexa skill icon](/icons/icon_108.png)

Get hot deals by duration

# Release note

## v0.1.0 - XX/XX/XXXX

### Usage

You can ask 

> - Alexa, demande à Readable skill name for the Alexa skill...
> - ...


-------------------------------

## Requirements

IF NEEDED

## Useful

- [Alexa developer console](https://developer.amazon.com/alexa/console/ask)
- [AWS Lambda console](https://eu-west-1.console.aws.amazon.com/lambda/home?region=eu-west-1)
- [Icon generation](https://developer.amazon.com/fr/docs/tools/icon-builder.html)

### Alexa developer console

- Add at least one intent
- If needed, go to `Interfaces` to enable `Audio Player` and `Display Interface`
- Don't forget to save and build the model

### Lambda 

- Alexa skill kit is not available in Paris AWS datacenter (available in Ireland)
- Load the zip file obtained in `build` (generated with `package.sh`)
- Make sure you put `Get hot dealsGet hot deals_skill.handler` in Gestionnaire
- Select **Alexa Skills Kit** in `Designer`
- Put the skill id that you got from the `Alexa developer console` > Endpoint
- Copy the ARN of the function from the upper right corner
- Paste it in > Endpoint > Default Region in `Alexa developer console`

## TODO

- [ ] 