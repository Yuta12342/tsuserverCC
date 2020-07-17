# tsuserverCC, an Attorney Online server.
#
# Copyright (C) 2020 Kaiser <kaiserkaisie@gmail.com>
#
# Derivative of tsuserver3, an Attorney Online server. Copyright (C) 2016 argoneus <argoneuscze@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import logging
import yaml

class HubManager:
    """
    Handles storing and loading areas for hubs.
    """
    def __init__(self, server):
        self.server = server

	def loadhub(self, client, arg):
        hubname = f'storage/hub/{arg}.yaml'
        new = not os.path.exists(hubname)
        if new:
            client.send_ooc('No hub with that name found.')
            return
		else:
			with open(hubname, 'r') as chars:
				areas = yaml.safe_load(chars)
			self.clearsub(client)
			for item in areas:
				sub = self.server.area_manager.Area(client.area.cur_subid, self.server, item['area'],
						  item['background'], bg_lock=False, evidence_mod='CM', locking_allowed=True, iniswap_allowed=True, 
						  showname_changes_allowed=True, shouts_allowed=True, jukebox=False, abbreviation='', non_int_pres_only=False)
				client.area.subareas.append(sub)
				sub.owners.add(client)
				client.area.cur_subid += 1
			area_list = []
			lobby = self.server.area_manager.default_area()
			area_list.append(lobby.name)
			area_list.append(client.area.name)
				for a in client.area.subareas:
					area_list.append(a.name)
			client.area.sub_arup_cms()
			client.area.sub_arup_status()
			client.server.send_all_cmd_pred('FA', *area_list, pred=lambda x: x.area == client.area or x.area in client.area.subareas)
		
	def savehub(self, client, arg):
		hubname = f'storage/hub/{arg}.yaml'
        new = not os.path.exists(hubname)
        if not new:
            os.remove(hubname)
		hub = dict()
		for area in client.area.subareas:
			hub['area'] = area.name
			hub['background'] = area.background
		with open(hubname, 'w', encoding='utf-8') as hubfile:
			yaml.dump(hub, hubfile)
	
	def removesub(self, client):
		destroyed = client.area
		hub = destroyed.hub
		destroyedclients = set()
		for c in destroyed.clients:
			if c in destroyed.owners:
				destroyed.owners.remove(c)
			destroyedclients.add(c)
		for c in destroyedclients:
			if c in destroyed.clients:
				c.change_area(hub)
				c.send_ooc(f'You were moved to {hub.name} from {destroyed.name} because it was destroyed.')
		hub.subareas.remove(destroyed)
		old_sublist = []
		for sub in hub.subareas:
			old_sublist.append(sub)
		hub.subareas.clear()
		hub.cur_subid = 1
		for sub in old_sublist:
			sub.id = hub.cur_subid
			sub.abbreviation = f'H{hub.hubid}S{sub.id}'
			hub.subareas.append(sub)
			hub.cur_subid += 1
		area_list = []
		lobby = self.server.area_manager.default_area()
		area_list.append(lobby.name)
		area_list.append(hub.name)
		for sub in hub.subareas:
			area_list.append(sub.name)
		client.server.send_all_cmd_pred('FA', *area_list, pred=lambda x: x.area == hub or x.area in hub.subareas)
		hub.sub_arup_cms()
		hub.sub_arup_status()
	
	def clearsub(self, client)
		hub.client.area
		destroyedclients = set()
		for sub in hub.subareas:
			for c in sub.clients:
				if c in sub.owners:
					sub.owners.remove(c)
				destroyedclients.add(c)
		for c in destroyedclients:
			if c in destroyed.clients:
				c.change_area(hub)
				c.send_ooc(f'You were moved to {hub.name} because the hub was cleared.')
		hub.subareas.clear()
		hub.cur_subid = 1
		area_list = []
		lobby = self.server.area_manager.default_area()
		area_list.append(lobby.name)
		area_list.append(hub.name)
		client.server.send_all_cmd_pred('FA', *area_list, pred=lambda x: x.area == hub or x.area in hub.subareas)
		hub.sub_arup_cms()
		hub.sub_arup_status()

	def addsub(self, client, arg)
		index = 0
		for area in client.server.area_manager.areas:
			if area.is_hub:
				index += 1
				area.hubid = index
		if client.area.is_hub:
			if client.area.cur_subid > 50:
				raise ClientError('You cannot have more than 50 areas in a hub.')
			elif client.area.name.startswith('Arcade') or client.area.name.startswith('User'):
				if client.area.cur_subid > 15:
					raise ClientError('Cannot have more than 15 areas in this hub.')
			new_id = client.area.cur_subid
			client.area.cur_subid += 1
		else:
			if client.area.hub.cur_subid > 50:
				raise ClientError('You cannot have more than 50 areas in a hub.')
			elif client.area.hub.name.startswith('Arcade') or client.area.hub.name.startswith('User'):
				if client.area.hub.cur_subid > 15:
					raise ClientError('Cannot have more than 15 areas in this hub.')
			new_id = client.area.hub.cur_subid
			client.area.hub.cur_subid += 1
		if len(arg) == 0:
			newsub = client.server.area_manager.Area(new_id, client.server, name=f'Area {new_id}', background='MeetingRoom', bg_lock=False, evidence_mod='CM', locking_allowed=True, iniswap_allowed=True, showname_changes_allowed=True, shouts_allowed=True, jukebox=False, abbreviation='', non_int_pres_only=False)
		else:
			newsub = client.server.area_manager.Area(new_id, client.server, name=arg, background='MeetingRoom', bg_lock=False, evidence_mod='CM', locking_allowed=True, iniswap_allowed=True, showname_changes_allowed=True, shouts_allowed=True, jukebox=False, abbreviation='', non_int_pres_only=False)
		newsub.sub = True
		if client.area.is_hub:
			newsub.hub = client.area
			client.area.subareas.append(newsub)
		else:
			newsub.hub = client.area.hub
			client.area.hub.subareas.append(newsub)
		if newsub.hub.name.startswith('Arcade'):
			newsub.abbreviation = f'HAS{new_id}'
		elif newsub.hub.name.startswith('User'):
			newsub.abbreviation = f'HUS{new_id}'
		else:
			newsub.abbreviation = f'H{newsub.hub.hubid}S{new_id}'
		#client.server.send_all_cmd_pred('CT', '{}'.format(client.server.config['hostname']),f'=== Announcement ===\r\nA new area has been created.\n[{new_id}] {arg}\r\n==================', '1')
		area_list = []
		lobby = self.server.area_manager.default_area()
		area_list.append(lobby.name)
		if client.area.is_hub:
			area_list.append(client.area.name)
			for a in client.area.subareas:
				area_list.append(a.name)
		else:
			area_list.append(client.area.hub.name)
			for a in client.area.hub.subareas:
				area_list.append(a.name)
		if client in client.area.owners:
			newsub.owners.append(client)
			newsub.status = client.area.status
			newsub.hub.sub_arup_cms()
			newsub.hub.sub_arup_status()
		client.server.send_all_cmd_pred('FA', *area_list, pred=lambda x: x.area == newsub.hub or x.area in newsub.hub.subareas)