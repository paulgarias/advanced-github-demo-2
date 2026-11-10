# Maintainer setup

One-time repository configuration. Contributors do not need any of this; it is for
whoever owns the repository. Replace `quantumdot/advanced-github-demo-2` with your
own `owner/repo` if you fork the project.

!!! tip
    `scripts/configure-repo.ps1` applies the branch ruleset, creates the `testpypi`
    environment and adds the workshop labels. The steps below cover the parts that
    have to be done in a web browser.

## Publishing to TestPyPI with a Trusted Publisher

Releases are published by `.github/workflows/release.yml` using
[Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (OIDC). GitHub proves
the identity of the workflow to the package index, so **no API token is stored** in the
repository.

[TestPyPI](https://test.pypi.org) is a sandbox copy of PyPI, so nothing here touches
the real index.

### 1. Create a TestPyPI account

Register at <https://test.pypi.org/account/register/>. This is a separate account from
pypi.org. Verify your email and enable two-factor authentication.

### 2. Register a pending publisher

The `statlite` project does not exist on TestPyPI yet, so register a *pending*
publisher. It creates the project the first time the workflow publishes.

1. Open <https://test.pypi.org/manage/account/publishing/>
   (*Account settings → Publishing*).
2. In the **GitHub** form, enter:

    | Field | Value |
    |---|---|
    | PyPI Project Name | `statlite` |
    | Owner | `quantumdot` |
    | Repository name | `advanced-github-demo-2` |
    | Workflow name | `release.yml` |
    | Environment name | `testpypi` |

3. Click **Add**. The publisher is listed as *pending*.

!!! warning
    A pending publisher does **not** reserve the project name. If someone else
    registers `statlite` before your first publish, the pending publisher is
    invalidated.

### 3. Check the GitHub environment

The environment name must match exactly. Check *Settings → Environments* for
`testpypi` (created by `scripts/configure-repo.ps1`). Optionally add yourself as a
**required reviewer** so every publish waits for a manual approval.

### 4. Publish a release

The release workflow only accepts tags that are on `main`, and the package version is
derived from the tag by `hatch-vcs`.

```bash
git switch main && git pull
git tag -a v0.1.0 -m "v0.1.0"
git push origin v0.1.0
```

Watch the **Release** run in the *Actions* tab. When `Publish to TestPyPI` succeeds the
package appears at <https://test.pypi.org/project/statlite/> and the pending publisher
becomes a normal one. Verify with:

```bash
pip install -i https://test.pypi.org/simple/ statlite
```

### Troubleshooting

- **`invalid-publisher` or a "trusted publisher" error:** one of the owner, repository,
  workflow file name or environment name does not match what you registered. If the
  repository is renamed or transferred, update the publisher.
- **"File already exists":** TestPyPI never allows a version to be reused, even after a
  deletion. Tag a new version, for example `v0.1.1` or a pre-release such as
  `v0.2.0rc1`.
- **The release job is skipped or fails before publishing:** the tag is not on `main`.

## Coverage reporting with Codecov

The `test` job in `.github/workflows/ci.yml` runs `pytest` (which writes `coverage.xml`)
and uploads it to [Codecov](https://about.codecov.io) from the Python 3.13 run. Codecov
then comments on pull requests and adds `codecov/project` and `codecov/patch` status
checks.

Coverage is enforced locally and in CI by `--cov-fail-under=90`. Codecov adds history,
per-line diffs on pull requests and the README badge. The upload step uses
`fail_ci_if_error: false`, so an upload problem never blocks a merge.

### 1. Sign up and install the app

1. Go to <https://app.codecov.io/signup> and choose **Sign up with GitHub**.
2. Authorize Codecov, and install the [Codecov GitHub app](https://github.com/apps/codecov)
   on your account or organization. Give it access to this repository.
3. In Codecov, open the repository list. If the repository is missing, click
   **Not Configured**, or wait a moment for the first sync.

### 2. Add the upload token

1. In Codecov, click **Configure** (or **Setup repo**) for the repository and copy the
   **repository upload token**.
2. In GitHub, open *Settings → Secrets and variables → Actions → New repository secret*
   and add:

    | Name | Value |
    |---|---|
    | `CODECOV_TOKEN` | the token you copied |

Or with the GitHub CLI:

```bash
gh secret set CODECOV_TOKEN --repo quantumdot/advanced-github-demo-2
```

!!! note
    Dependabot pull requests cannot read normal Actions secrets. To get coverage on
    Dependabot PRs, also add `CODECOV_TOKEN` under *Settings → Secrets and variables →
    Dependabot*.

### 3. Run CI and check the result

Push a branch or open a pull request. In the **Test (py3.13)** job, the
*Upload coverage to Codecov* step should end with an upload confirmation. After the
first run on `main` you should see:

- coverage on the repository dashboard at
  `https://app.codecov.io/gh/quantumdot/advanced-github-demo-2`
- a coverage comment and `codecov/patch` / `codecov/project` checks on pull requests
- the badge in the README showing a percentage instead of "unknown"

If the dashboard stays empty, check that the default branch is set to `main` under
*Configuration → General* in Codecov.

### Optional: make Codecov a required check

By default the Codecov statuses are informational. To enforce them, add
`codecov/patch` and `codecov/project` to the required status checks in the ruleset
(`.github/rulesets/protect-main.json`). Do this only after they have appeared on at
least one pull request, since GitHub can only require checks it has already seen.

### Troubleshooting

- **"Token required" or upload skipped:** `CODECOV_TOKEN` is missing or was added to the
  wrong place (environment secret vs. repository secret).
- **Upload fails on pull requests from forks:** Actions secrets are not shared with
  forks. For public repositories, Codecov supports
  [tokenless uploads for forks](https://docs.codecov.com/docs/codecov-uploader#supporting-token-less-uploads-for-forks-of-open-source-repos-using-codecov).
- **No comment on the pull request:** confirm the Codecov GitHub app is installed for
  this repository.

## Archiving releases on Zenodo (DOI)

[Zenodo](https://zenodo.org) archives a snapshot of the repository for every GitHub
Release and mints a DOI, so the exact version used in a paper can be cited. GitHub
documents the integration under
[Referencing and citing content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).

Requirements: the repository is **public**, and has a license (`LICENSE`) and a
`CITATION.cff`.

!!! tip
    Rehearse first on <https://sandbox.zenodo.org>. It works the same way, but records
    can be deleted, unlike on production Zenodo. Use a separate login and link it to
    GitHub on the sandbox site.

### 1. Link Zenodo to GitHub

1. Go to <https://zenodo.org/login> and click **Log in with GitHub**.
2. Review the permissions and click **Authorize zenodo**.

### 2. Enable the repository

1. Open <https://zenodo.org/account/settings/github/> (profile menu → **GitHub**).
2. Click **Sync now** so the repository list is current.
3. Find `quantumdot/advanced-github-demo-2` and switch its toggle to **On**.

!!! warning
    Do this **before** creating the release you want archived. Zenodo only archives
    releases published after the repository is enabled. Earlier tags and releases are
    not archived retroactively.

### 3. Publish a release

The `Release` workflow creates a GitHub Release when a `v*` tag is pushed, which is
what triggers Zenodo. Zenodo archives the release, not a bare tag.

```bash
git switch main && git pull
git tag -a v0.1.0 -m "v0.1.0"
git push origin v0.1.0
```

After a minute or two the release appears on the Zenodo GitHub settings page, with a
new record under <https://zenodo.org/me/uploads>. If it does not, open
*Settings → Webhooks* in the GitHub repository and check the recent deliveries of the
Zenodo webhook. A failed delivery can be redelivered from there.

### 4. Record the DOI

Each release gets its own **version DOI**, and the project gets one **concept DOI**
that always points to the latest version. Cite the version DOI in a paper, and use the
concept DOI in the README badge.

1. Copy the concept DOI from the Zenodo record, for example `10.5281/zenodo.1234567`.
2. Add the badge to `README.md`:

    ```markdown
    [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
    ```

3. Add `doi: 10.5281/zenodo.1234567` to `CITATION.cff` so GitHub's **Cite this
   repository** button includes it.

The DOI only exists after the first release is archived, so these two edits go in a
follow-up pull request.

### Metadata and authors

Zenodo reads `CITATION.cff` (it supports a subset of the format) to fill in the title,
authors, license, keywords and description. Two things to know:

- If the repository also has a `.zenodo.json` file, Zenodo uses **only** that file and
  ignores `CITATION.cff`. Keep just one source of truth.
- Zenodo expects people as `given-names` and `family-names`, optionally with an
  `orcid`. The current file lists the workshop as an organization name. Before the
  first archived release, change it to the real author(s):

    ```yaml
    authors:
      - given-names: Ada
        family-names: Lovelace
        orcid: "https://orcid.org/0000-0000-0000-0000"
    ```

  Metadata on a published Zenodo record can be edited by hand, but the DOI and archived
  files cannot be changed.

## Other one-time settings

- **GitHub Pages:** after the first `Docs` workflow run creates the `gh-pages` branch,
  set *Settings → Pages → Source* to **Deploy from a branch**, `gh-pages`, `/ (root)`.
