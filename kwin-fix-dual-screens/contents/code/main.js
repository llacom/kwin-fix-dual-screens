workspace.clientAdded.connect(function(client) {
    function fixdualscreen() {

	if (workspace.numScreens === 1) return;

	if (client.screen > 0) {
	    callDBus("org.fixscreen", "/org/fixscreen", "org.fixscreen", "setActivities", client.windowId, "");
	    client.onAllDesktops = true;
	}
	if (client.screen === 0) {
	    callDBus("org.fixscreen", "/org/fixscreen", "org.fixscreen", "setActivities", client.windowId, workspace.currentActivity);
	    client.onAllDesktops = false;
	}
    }

    client.screenChanged.connect(fixdualscreen);
    fixdualscreen();
});
