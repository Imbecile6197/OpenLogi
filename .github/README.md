# OpenLogi česky

Fork projektu [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) – otevřené alternativy k Logi Options+ pro nastavení myší a klávesnic Logitech (přemapování tlačítek, DPI, SmartShift). Bez účtu a bez telemetrie.

Tento fork přidává:

- **českou lokalizaci** celého rozhraní (všech 580 textů),
- **viditelné tlačítko „Spárovat Bolt / Unifying…“** v přehledu zařízení i v detailu zařízení, takže párování přes přijímač Logi Bolt nebo Unifying je vždy po ruce,
- český popis a klíčová slova spouštěče v nabídce aplikací,
- balíček RPM pro Fedoru.

Čeština je navržená i do původního projektu v [AprilNEA/OpenLogi#1669](https://github.com/AprilNEA/OpenLogi/pull/1669). Tlačítko párování zůstává jen v tomto forku.

![České rozhraní](https://raw.githubusercontent.com/Imbecile6197/OpenLogi/pr-assets/czech-ui.png)

## Instalace na Fedoru

Stáhněte balíček `.rpm` z [Releases](https://github.com/Imbecile6197/OpenLogi/releases), zavřete OpenLogi a v terminálu ve složce se staženým souborem spusťte:

```sh
sudo dnf install ./openlogi-0.8.11-1.cs3.fc44.x86_64.rpm
systemctl --user daemon-reload
systemctl --user enable --now openlogi-agent.service
openlogi-desktop
```

Balíček je sestavený pro Fedoru 44 (x86_64) a nahradí případnou starší instalaci OpenLogi. Obsahuje aplikaci, službu na pozadí `openlogi-agent`, spouštěč, ikony a pravidla udev pro přístup k přijímačům.

Jazyk se nastaví automaticky podle systému, případně ručně v **Nastavení → Vzhled → Jazyk → Čeština**.

## Párování přes Bolt / Unifying

1. Připojte přijímač a ukončete Solaar nebo jiného správce zařízení Logitech.
2. Přepněte myš či klávesnici do režimu párování.
3. Klikněte na **Spárovat Bolt / Unifying…** a vyberte nalezené zařízení.
4. Postupujte podle pokynů pro ověřovací kód nebo posloupnost kliknutí.

Při více zapojených přijímačích se použije první podporovaný – pro párování nechte připojený jen ten požadovaný. Přímé Bluetooth připojení se páruje v nastavení systému.

## Sestavení ze zdrojů

Větev `cs-bolt` obsahuje všechny úpravy. Na Fedoře:

```sh
sudo dnf install gcc-c++ clang clang-devel systemd-devel libxkbcommon-devel libxkbcommon-x11-devel openssl-devel libzstd-devel rpm-build
cargo build --release -p openlogi -p openlogi-desktop -p openlogi-overlay -p openlogi-agent
rpmbuild -bb packaging/linux/openlogi-cs.spec --define "_srcroot $PWD" --define "_rpmdir $PWD/target"
```

Hotový balíček najdete v `target/x86_64/`.

## Licence

Stejně jako původní projekt: Apache-2.0 nebo MIT.
