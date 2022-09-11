rebuild:
	sam build

deploy:
	make rebuild
	sam deploy --resolve-s3 --profile $(profile) \
	--parameter-overrides \
	'ParameterKey=VerificationToken,ParameterValue=$(VerificationToken) \
	ParameterKey=SlackBotToken,ParameterValue=$(SlackBotToken) \
	ParameterKey=SlackSigningSecret,ParameterValue=$(SlackSigningSecret) \
	ParameterKey=GithubToken,ParameterValue=$(GithubToken) \
	ParameterKey=GithubRepo,ParameterValue=$(GithubRepo)'

delete:
	sam delete --profile $(profile)
