# Copyright (C) 2022 - 2023 Alessandro Iepure
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gtk, Adw, GObject

@Gtk.Template(resource_path="/me/iepure/devtoolbox/ui/views/px_to_rem_converter.ui")
class PxToRemConverterView(Adw.Bin):
    __gtype_name__ = "PxToRemConverterView"

    # Template elements
    _px_entry = Gtk.Template.Child()
    _rem_entry = Gtk.Template.Child()
    _root_font_size_entry = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        # Signals
        self._px_entry.connect("changed", self._on_px_changed)
        self._rem_entry.connect("changed", self._on_rem_changed)
        self._root_font_size_entry.connect("changed", self._on_root_font_size_changed)

    def _on_px_changed(self, user_data: GObject.GPointer):
        self._convert_px_to_rem()

    def _on_rem_changed(self, user_data: GObject.GPointer):
        self._convert_rem_to_px()

    def _on_root_font_size_changed(self, user_data: GObject.GPointer):
        self._convert_px_to_rem()

    def _convert_px_to_rem(self):
        try:
            px_value = float(self._px_entry.get_text())
            root_font_size = float(self._root_font_size_entry.get_text())
            rem_value = px_value / root_font_size
            self._rem_entry.set_text(str(rem_value))
        except ValueError:
            pass

    def _convert_rem_to_px(self):
        try:
            rem_value = float(self._rem_entry.get_text())
            root_font_size = float(self._root_font_size_entry.get_text())
            px_value = rem_value * root_font_size
            self._px_entry.set_text(str(px_value))
        except ValueError:
            pass
