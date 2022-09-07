rebuild:
	sam build

deploy:
	make rebuild
	sam deploy --resolve-s3 --profile $(profile) --parameter-overrides 'ParameterKey=VerificationToken,ParameterValue=$(VerificationToken)'

delete:
	sam delete --profile $(profile)
