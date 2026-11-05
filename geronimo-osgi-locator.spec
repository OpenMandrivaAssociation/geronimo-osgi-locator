Name:		geronimo-osgi-locator
Version:	1.0
Release:	1
Summary:	Geronimo OSGi provider locator
Group:		Development/Java
License:	ASL 2.0
URL:		https://geronimo.apache.org/
Source0:	https://repo1.maven.org/maven2/org/apache/geronimo/specs/geronimo-osgi-locator/%{version}/geronimo-osgi-locator-%{version}-sources.jar
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	osgi-core
BuildRequires:	geronimo-osgi-registry
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

%description
ProviderLocator used by Geronimo specification jars to find
implementations, including through the OSGi registry when a framework
is present.

%prep
%setup -q -c
mkdir -p src/main/java
mv org src/main/java/
cp -a META-INF/LICENSE LICENSE
cp -a META-INF/NOTICE NOTICE
python - %{version} <<'PY'
import sys
from pathlib import Path
version = sys.argv[1]
Path("pom.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.apache.geronimo.specs</groupId>
  <artifactId>geronimo-osgi-locator</artifactId>
  <version>{version}</version>
  <packaging>jar</packaging>
  <name>Geronimo OSGi provider locator</name>
  <dependencies>
    <dependency>
      <groupId>org.apache.geronimo.specs</groupId>
      <artifactId>geronimo-osgi-registry</artifactId>
      <version>{version}</version>
      <scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>org.osgi</groupId>
      <artifactId>osgi.core</artifactId>
      <scope>provided</scope>
    </dependency>
  </dependencies>
</project>
""")
PY

%files -f .mfiles
%doc LICENSE NOTICE
