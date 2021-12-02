Gabriel Kiprono
CSC 4585


Security weaknesses in Workshop3.values.yaml

1. Hard coded secret
    found in following:
    line 19 variable sat_user
    line 20 variable sat_pass
    line 21 variable sat_email
    line 93 variable katello_user
    line 186 variable rootpw

2. Admin by default violation
    found in following:
    line 19 variable sat_user
    line 93 variable katello_user

3. No integrity check
    found in the following:
    line 82 variable sat_manifest
    line 91 variable epel_repo_installer
    line 148 variable epel_release_rpm

4. Use of HTTP without SSL/TLS
    found in the following lines
    line 86 variable foreman_repository_base
    line 87 variable foreman_plugin_repository_base
    line 104 variable content_rhel_url
    line 107 variable content_sattools_url
    line 156 variable test_sync_repositories_url_template
    line 188 variable vmm_kss_os

5. 