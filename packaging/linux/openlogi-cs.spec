# Repackages prebuilt release binaries of the Czech OpenLogi build.
# Usage (from the repository root, after `cargo build --release`):
#   rpmbuild -bb packaging/linux/openlogi-cs.spec --define "_srcroot $PWD" --define "_rpmdir $PWD/target"

%global debug_package %{nil}
%global __strip /bin/true

Name:           openlogi
Version:        0.8.11
Release:        1.cs3%{?dist}
Summary:        Logitech HID++ device control (Czech build with visible Bolt pairing)
License:        Apache-2.0 OR MIT
URL:            https://github.com/AprilNEA/OpenLogi

Requires:       glibc >= 2.43
Requires:       fontconfig freetype libxkbcommon libxkbcommon-x11 libxcb
Requires:       libwayland-client libwayland-cursor libglvnd-egl vulkan-loader
Requires:       systemd dbus

%description
Local Czech build of OpenLogi with visible Bolt / Unifying pairing buttons.
Remap buttons, DPI and SmartShift on Logitech devices. No account, no
telemetry; configuration lives in a plain TOML file.

%install
S="%{_srcroot}"
for b in openlogi openlogi-desktop openlogi-overlay openlogi-agent; do
  install -Dm0755 "$S/target/release/$b" %{buildroot}%{_bindir}/$b
done
install -Dm0644 "$S"/packaging/linux/udev/70-openlogi.rules %{buildroot}/etc/udev/rules.d/70-openlogi.rules
install -Dm0644 "$S"/packaging/linux/systemd/openlogi-agent.service %{buildroot}%{_userunitdir}/openlogi-agent.service
install -Dm0644 "$S"/packaging/linux/desktop/openlogi.desktop %{buildroot}%{_datadir}/applications/openlogi.desktop
install -Dm0644 "$S"/design/icon/openlogi.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/openlogi.png
for s in 512 256 128 64 48 32 16; do
  install -Dm0644 "$S"/design/icon/openlogi-$s.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/openlogi.png
done
install -Dm0644 "$S"/LICENSE-APACHE %{buildroot}%{_datadir}/licenses/openlogi/LICENSE-APACHE
install -Dm0644 "$S"/LICENSE-MIT %{buildroot}%{_datadir}/licenses/openlogi/LICENSE-MIT

%post
if command -v udevadm >/dev/null 2>&1; then
  udevadm control --reload-rules
  udevadm trigger --subsystem-match=hidraw
  udevadm trigger --subsystem-match=input
  udevadm trigger --subsystem-match=misc --attr-match=name=uinput 2>/dev/null || true
  udevadm settle 2>/dev/null || true
fi
gtk-update-icon-cache -qtf %{_datadir}/icons/hicolor 2>/dev/null || true
update-desktop-database -q %{_datadir}/applications 2>/dev/null || true

%postun
if command -v udevadm >/dev/null 2>&1; then
  udevadm control --reload-rules
  udevadm trigger --subsystem-match=hidraw
  udevadm settle 2>/dev/null || true
fi

%files
%{_bindir}/openlogi
%{_bindir}/openlogi-desktop
%{_bindir}/openlogi-overlay
%{_bindir}/openlogi-agent
%config(noreplace) /etc/udev/rules.d/70-openlogi.rules
%{_userunitdir}/openlogi-agent.service
%{_datadir}/applications/openlogi.desktop
%{_datadir}/icons/hicolor/*/apps/openlogi.png
%license %{_datadir}/licenses/openlogi/LICENSE-APACHE
%license %{_datadir}/licenses/openlogi/LICENSE-MIT

%changelog
* Mon Oct 05 2026 Local Czech build - 0.8.11-1.cs3
- Let the device-enabled caption wrap so the switch stays inside the card
* Mon Oct 05 2026 Local Czech build - 0.8.11-1.cs2
- Shorten Czech "Actions Ring" label to "Kruh akcí" so it fits the sidebar
* Sat Oct 03 2026 Local Czech build - 0.8.11-1.cs1
- Czech translation and visible Bolt / Unifying pairing button
