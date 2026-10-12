#define MyAppName "AN AI Relight V6"
#define MyAppVersion "6.0"
#define MyAppPublisher "AN AI Studio"
#define MyAppExeName "AN_AI_Relight.exe"

[Setup]
AppId={{AN-AI-RELIGHT-V6}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\AN AI Relight V6
DefaultGroupName={#MyAppName}

OutputDir=installer_output
OutputBaseFilename=AN_AI_Relight_V6_Setup

Compression=lzma
SolidCompression=yes

ArchitecturesInstallIn64BitMode=x64

PrivilegesRequired=admin

[Files]

Source: "build\AN_AI_Relight.exe"; DestDir: "{app}"; Flags: ignoreversion

Source: "runtime\*"; DestDir: "{app}\runtime"; Flags: ignoreversion recursesubdirs createallsubdirs

Source: "requirements.txt"; DestDir: "{app}"; Flags: ignoreversion


[Icons]

Name: "{commondesktop}\AN AI Relight V6"; Filename: "{app}\AN_AI_Relight.exe"

Name: "{group}\AN AI Relight V6"; Filename: "{app}\AN_AI_Relight.exe"


[Run]

Filename: "{app}\AN_AI_Relight.exe"; Description: "Launch AN AI Relight V6"; Flags: nowait postinstall skipifsilent


[UninstallDelete]

Type: filesandordirs; Name: "{app}"
