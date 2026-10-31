# OpenLogi česky (archivováno)

Tento fork projektu [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) už se nevyvíjí. **Používejte oficiální OpenLogi**, které je česky a umí párovat přes přijímač Logi Bolt i Unifying.

## Co se dostalo do oficiální verze

- Česká lokalizace celého rozhraní ([#1669](https://github.com/AprilNEA/OpenLogi/pull/1669), doplněná v [#1728](https://github.com/AprilNEA/OpenLogi/pull/1728), [#1850](https://github.com/AprilNEA/OpenLogi/pull/1850) a [#2034](https://github.com/AprilNEA/OpenLogi/pull/2034)).
- Oprava přetékajícího přepínače „Spravovat toto zařízení“ u delších překladů ([#1670](https://github.com/AprilNEA/OpenLogi/pull/1670)).

Párování spustíte tlačítkem **Přidat zařízení** na obrazovce Zařízení. Otevře výběr přijímače Bolt nebo Unifying.

## Instalace na Fedoru

Stáhněte balíček `.rpm` pro `linux-amd64` z [vydání OpenLogi](https://github.com/AprilNEA/OpenLogi/releases/latest) a nainstalujte ho:

```sh
sudo dnf install ./openlogi-v*-linux-amd64.rpm
systemctl --user enable --now openlogi-agent.service
```

Jazyk se nastaví automaticky podle systému, případně ručně v **Nastavení → Vzhled → Jazyk → Čeština**.

Starší balíčky tohoto forku zůstávají ke stažení v [Releases](https://github.com/Imbecile6197/OpenLogi/releases).
